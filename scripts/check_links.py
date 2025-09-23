#!/usr/bin/env python3
"""
Check accessibility of all URLs in resources.yaml
"""

import yaml
import requests
import json
import sys
from pathlib import Path
from typing import List, Dict, Any
from urllib.parse import urlparse
import time


def check_url(url: str, timeout: int = 10, max_retries: int = 2) -> Dict[str, Any]:
    """
    Check if a URL is accessible.

    Returns:
        Dict with 'accessible', 'status_code', 'error', and 'redirect_url' keys
    """
    result = {
        'accessible': False,
        'status_code': None,
        'error': None,
        'redirect_url': None
    }

    for attempt in range(max_retries + 1):
        try:
            # Try HEAD first (faster)
            response = requests.head(
                url,
                timeout=timeout,
                allow_redirects=True,
                headers={
                    'User-Agent': 'Engineering-Arsenal-LinkChecker/1.0'
                }
            )

            result['status_code'] = response.status_code

            # If HEAD fails with 405 (Method Not Allowed), try GET
            if response.status_code == 405:
                response = requests.get(
                    url,
                    timeout=timeout,
                    allow_redirects=True,
                    headers={
                        'User-Agent': 'Engineering-Arsenal-LinkChecker/1.0'
                    }
                )
                result['status_code'] = response.status_code

            # Check for redirects
            if response.url != url:
                result['redirect_url'] = response.url

            # Consider status codes < 400 as successful
            if response.status_code < 400:
                result['accessible'] = True
                return result
            else:
                result['error'] = f"HTTP {response.status_code}"

        except requests.exceptions.Timeout:
            result['error'] = f"Timeout after {timeout}s"
        except requests.exceptions.ConnectionError:
            result['error'] = "Connection failed"
        except requests.exceptions.SSLError:
            result['error'] = "SSL certificate error"
        except requests.exceptions.TooManyRedirects:
            result['error'] = "Too many redirects"
        except requests.exceptions.RequestException as e:
            result['error'] = f"Request error: {str(e)[:50]}"
        except Exception as e:
            result['error'] = f"Unexpected error: {str(e)[:50]}"

        # Wait before retry (except on last attempt)
        if attempt < max_retries:
            time.sleep(1)

    return result


def check_all_links() -> bool:
    """Check all links in resources.yaml and report broken ones."""

    yaml_path = Path("data/resources.yaml")
    if not yaml_path.exists():
        print(f"❌ Resources file not found: {yaml_path}")
        return False

    # Load resources
    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading YAML: {e}")
        return False

    if 'resources' not in data:
        print("❌ No 'resources' key found in YAML")
        return False

    resources = data['resources']
    print(f"🔍 Checking {len(resources)} resources...")

    broken_links = []
    accessible_count = 0
    total_checked = 0

    for i, resource in enumerate(resources, 1):
        url = resource.get('url')
        resource_id = resource.get('id', f'resource_{i}')
        title = resource.get('title', 'Unknown')

        if not url:
            print(f"⚠️ {resource_id}: No URL specified")
            continue

        total_checked += 1
        print(f"🔗 [{i}/{len(resources)}] Checking {resource_id}...")

        # Check URL accessibility
        result = check_url(url)

        if result['accessible']:
            accessible_count += 1
            status_msg = f"✅ {resource_id}: OK"
            if result['redirect_url']:
                status_msg += f" (redirected to {result['redirect_url']})"
            print(status_msg)
        else:
            broken_links.append({
                'id': resource_id,
                'title': title,
                'url': url,
                'status': result['status_code'],
                'error': result['error']
            })
            print(f"❌ {resource_id}: {result['error']} - {url}")

        # Small delay to be nice to servers
        time.sleep(0.5)

    # Report results
    print(f"\n📊 Link Check Results:")
    print(f"  • Total resources: {len(resources)}")
    print(f"  • Links checked: {total_checked}")
    print(f"  • Accessible: {accessible_count}")
    print(f"  • Broken: {len(broken_links)}")

    # Save broken links to JSON file for GitHub Actions
    broken_links_file = Path("broken_links.json")
    with open(broken_links_file, 'w', encoding='utf-8') as f:
        json.dump(broken_links, f, indent=2)

    if broken_links:
        print(f"\n❌ Broken Links:")
        for link in broken_links:
            print(f"  • {link['id']}: {link['error']} - {link['url']}")

        print(f"\n💾 Broken links saved to {broken_links_file}")
        return False  # Return False to indicate broken links found
    else:
        print(f"\n🎉 All links are working!")
        return True


def main():
    """Main execution function."""
    print("🔗 Starting link accessibility check...")

    try:
        success = check_all_links()
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())