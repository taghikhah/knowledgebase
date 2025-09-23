#!/usr/bin/env python3
"""
Analyze changes in a PR for GitHub Actions
"""

import yaml
import json
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Set


def get_git_diff() -> List[str]:
    """Get the list of changed files from git."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout.strip().split('\n') if result.stdout.strip() else []
        else:
            # Fallback for PR context
            result = subprocess.run(
                ['git', 'diff', '--name-only', 'origin/main', 'HEAD'],
                capture_output=True,
                text=True
            )
            return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except Exception as e:
        print(f"⚠️ Could not get git diff: {e}")
        return []


def load_resources(yaml_path: str) -> Dict[str, Any]:
    """Load resources from YAML file."""
    path = Path(yaml_path)
    if not path.exists():
        return {'resources': []}

    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {'resources': []}
    except Exception as e:
        print(f"⚠️ Error loading {yaml_path}: {e}")
        return {'resources': []}


def get_resource_by_id(resources: List[Dict[str, Any]], resource_id: str) -> Dict[str, Any]:
    """Find a resource by its ID."""
    for resource in resources:
        if resource.get('id') == resource_id:
            return resource
    return {}


def analyze_resources_changes() -> Dict[str, Any]:
    """Analyze changes to resources.yaml."""

    # Check if resources.yaml was changed
    changed_files = get_git_diff()
    if 'data/resources.yaml' not in changed_files:
        return {
            'new_resources': [],
            'modified_resources': [],
            'removed_resources': [],
            'validation_warnings': []
        }

    # Load current and previous versions
    current_data = load_resources('data/resources.yaml')
    current_resources = current_data.get('resources', [])

    # Try to get the previous version from git
    try:
        result = subprocess.run(
            ['git', 'show', 'HEAD~1:data/resources.yaml'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            previous_data = yaml.safe_load(result.stdout) or {'resources': []}
            previous_resources = previous_data.get('resources', [])
        else:
            # Fallback for PR context
            result = subprocess.run(
                ['git', 'show', 'origin/main:data/resources.yaml'],
                capture_output=True,
                text=True
            )
            previous_data = yaml.safe_load(result.stdout) if result.returncode == 0 else {'resources': []}
            previous_resources = previous_data.get('resources', [])
    except Exception as e:
        print(f"⚠️ Could not get previous version: {e}")
        previous_resources = []

    # Create ID sets for comparison
    current_ids = {r.get('id') for r in current_resources if r.get('id')}
    previous_ids = {r.get('id') for r in previous_resources if r.get('id')}

    # Find new, modified, and removed resources
    new_ids = current_ids - previous_ids
    removed_ids = previous_ids - current_ids
    potentially_modified_ids = current_ids & previous_ids

    new_resources = [r for r in current_resources if r.get('id') in new_ids]
    removed_resources = [r for r in previous_resources if r.get('id') in removed_ids]

    # Check for modifications
    modified_resources = []
    for resource_id in potentially_modified_ids:
        current_resource = get_resource_by_id(current_resources, resource_id)
        previous_resource = get_resource_by_id(previous_resources, resource_id)

        # Compare key fields (exclude auto-generated fields like github_stars)
        compare_fields = ['title', 'url', 'domains', 'type', 'maturity', 'tags', 'summary', 'why_useful', 'good_for']

        for field in compare_fields:
            if current_resource.get(field) != previous_resource.get(field):
                modified_resources.append(current_resource)
                break

    # Run validation and collect warnings
    validation_warnings = []
    try:
        result = subprocess.run(
            ['python', 'scripts/validate.py'],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            # Extract warnings from validation output
            output_lines = result.stdout.split('\n') + result.stderr.split('\n')
            for line in output_lines:
                if 'Warning' in line or '⚠️' in line:
                    validation_warnings.append(line.strip())
    except Exception as e:
        validation_warnings.append(f"Could not run validation: {e}")

    return {
        'new_resources': new_resources,
        'modified_resources': modified_resources,
        'removed_resources': removed_resources,
        'validation_warnings': validation_warnings[:10]  # Limit to top 10
    }


def main():
    """Main execution function."""
    print("🔍 Analyzing PR changes...")

    try:
        analysis = analyze_resources_changes()

        # Print summary
        print(f"📊 Analysis Results:")
        print(f"  • New resources: {len(analysis['new_resources'])}")
        print(f"  • Modified resources: {len(analysis['modified_resources'])}")
        print(f"  • Removed resources: {len(analysis['removed_resources'])}")
        print(f"  • Validation warnings: {len(analysis['validation_warnings'])}")

        if analysis['new_resources']:
            print(f"\n🆕 New Resources:")
            for resource in analysis['new_resources']:
                print(f"  • {resource.get('title', 'Unknown')} ({resource.get('id', 'unknown')})")

        if analysis['modified_resources']:
            print(f"\n✏️ Modified Resources:")
            for resource in analysis['modified_resources']:
                print(f"  • {resource.get('title', 'Unknown')} ({resource.get('id', 'unknown')})")

        if analysis['removed_resources']:
            print(f"\n🗑️ Removed Resources:")
            for resource in analysis['removed_resources']:
                print(f"  • {resource.get('title', 'Unknown')} ({resource.get('id', 'unknown')})")

        if analysis['validation_warnings']:
            print(f"\n⚠️ Validation Warnings:")
            for warning in analysis['validation_warnings']:
                print(f"  • {warning}")

        # Save analysis to JSON for GitHub Actions
        analysis_file = Path("pr_analysis.json")
        with open(analysis_file, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, default=str)

        print(f"\n💾 Analysis saved to {analysis_file}")
        return 0

    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())