#!/usr/bin/env python3
"""
Update GitHub star counts for repositories in resources.yaml
"""

import yaml
import requests
import os
import sys
from pathlib import Path
from typing import Dict, Any


def update_github_stars(github_token: str) -> bool:
    """Update GitHub star counts for all repositories."""

    yaml_path = Path("data/resources.yaml")
    if not yaml_path.exists():
        print(f"❌ Resources file not found: {yaml_path}")
        return False

    # Load resources
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if 'resources' not in data:
        print("❌ No 'resources' key found in YAML")
        return False

    # GitHub API headers
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Engineering-Arsenal-Bot/1.0'
    }

    updated_count = 0
    total_repos = 0

    for resource in data['resources']:
        url = resource.get('url', '')
        resource_id = resource.get('id', 'unknown')

        # Skip non-GitHub URLs or specific paths
        if 'github.com' not in url or any(path in url for path in ['/tree/', '/blob/', '/issues', '/wiki']):
            continue

        total_repos += 1

        try:
            # Extract owner/repo from GitHub URL
            parts = url.replace('https://github.com/', '').strip('/').split('/')
            if len(parts) < 2:
                print(f"⚠️ Invalid GitHub URL format for {resource_id}: {url}")
                continue

            owner, repo = parts[0], parts[1]

            # Fetch current stars
            api_url = f'https://api.github.com/repos/{owner}/{repo}'
            response = requests.get(api_url, headers=headers, timeout=15)

            if response.status_code == 200:
                repo_data = response.json()
                new_stars = repo_data.get('stargazers_count', 0)
                old_stars = resource.get('github_stars', 0)

                if new_stars != old_stars:
                    resource['github_stars'] = new_stars
                    updated_count += 1
                    change = "+" if new_stars > old_stars else ""
                    print(f"✅ Updated {resource_id}: {old_stars} -> {new_stars} stars ({change}{new_stars - old_stars})")
                else:
                    print(f"ℹ️ {resource_id}: {new_stars} stars (unchanged)")

            elif response.status_code == 404:
                print(f"⚠️ Repository not found for {resource_id}: {url}")
            elif response.status_code == 403:
                print(f"⚠️ Rate limited or forbidden for {resource_id}: {url}")
                if 'X-RateLimit-Remaining' in response.headers:
                    remaining = response.headers['X-RateLimit-Remaining']
                    reset_time = response.headers.get('X-RateLimit-Reset', 'unknown')
                    print(f"   Rate limit remaining: {remaining}, resets at: {reset_time}")
            else:
                print(f"⚠️ Failed to fetch stars for {resource_id}: HTTP {response.status_code}")

        except requests.RequestException as e:
            print(f"❌ Network error for {resource_id}: {str(e)[:100]}")
        except Exception as e:
            print(f"❌ Error processing {resource_id}: {str(e)[:100]}")

    # Save updated data if changes were made
    if updated_count > 0:
        try:
            with open(yaml_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
            print(f"\n🎉 Successfully updated {updated_count}/{total_repos} repositories")
            return True
        except Exception as e:
            print(f"❌ Error saving updated YAML: {e}")
            return False
    else:
        print(f"\nℹ️ No star count updates needed for {total_repos} repositories")
        return True


def main():
    """Main execution function."""
    github_token = os.environ.get('GITHUB_TOKEN')

    if not github_token:
        print("❌ GITHUB_TOKEN environment variable not set")
        return 1

    print("🌟 Starting GitHub star count update...")

    try:
        success = update_github_stars(github_token)
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())