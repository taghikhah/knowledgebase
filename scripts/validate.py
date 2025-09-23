#!/usr/bin/env python3
"""
Validate resources.yaml schema and content quality.
Run this before committing changes to catch issues early.
"""

import yaml
import re
import requests
from pathlib import Path
from typing import Dict, List, Any, Set
from urllib.parse import urlparse
from datetime import datetime

# Schema definition
REQUIRED_FIELDS = [
    "id",
    "title",
    "url",
    "domain",
    "type",
    "maturity",
    "effort",
    "tags",
    "published",
    "last_updated",
    "summary",
    "why_useful",
    "good_for",
]

OPTIONAL_FIELDS = [
    "source_owner",
    "license",
    "github_stars",
    "language",
    "setup_time_minutes",
    "prerequisites",
    "use_cases",
    "related",
]

VALID_DOMAINS = [
    "LLMOps-RAG",
    "ML-Engineering",
    "DevOps-SRE",
    "Data-Engineering",
    "Security",
    "Systems-Tools",
    "System-Design",
    "Productivity",
]

VALID_TYPES = [
    "Repo",
    "Article",
    "Guide",
    "Talk",
    "Tool",
    "Framework",
    "Dataset",
    "Spec",
]

VALID_MATURITY = ["Battle-tested", "Emerging", "Experimental"]
VALID_EFFORT = ["Low", "Medium", "High"]
VALID_GOOD_FOR = ["learning", "production", "POCs", "research", "templates"]


class ValidationError(Exception):
    """Custom exception for validation errors."""

    pass


class ResourceValidator:
    """Validates individual resources and the collection as a whole."""

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.seen_ids = set()
        self.seen_urls = set()

    def validate_resource(self, resource: Dict[str, Any], index: int) -> None:
        """Validate a single resource entry."""
        resource_id = resource.get("id", f"resource_{index}")

        try:
            self._validate_required_fields(resource, resource_id)
            self._validate_field_types(resource, resource_id)
            self._validate_field_values(resource, resource_id)
            self._validate_uniqueness(resource, resource_id)
            self._validate_content_quality(resource, resource_id)
            self._validate_url_format(resource, resource_id)

        except ValidationError as e:
            self.errors.append(f"Resource '{resource_id}': {e}")

    def _validate_required_fields(
        self, resource: Dict[str, Any], resource_id: str
    ) -> None:
        """Check that all required fields are present."""
        missing_fields = [field for field in REQUIRED_FIELDS if field not in resource]
        if missing_fields:
            raise ValidationError(f"Missing required fields: {missing_fields}")

    def _validate_field_types(self, resource: Dict[str, Any], resource_id: str) -> None:
        """Validate field data types."""
        # String fields
        string_fields = [
            "id",
            "title",
            "url",
            "type",
            "maturity",
            "effort",
            "summary",
            "why_useful",
        ]
        for field in string_fields:
            if field in resource and not isinstance(resource[field], str):
                raise ValidationError(f"Field '{field}' must be a string")

        # List fields
        list_fields = ["domain", "tags", "good_for"]
        for field in list_fields:
            if field in resource and not isinstance(resource[field], list):
                raise ValidationError(f"Field '{field}' must be a list")

        # Integer fields
        int_fields = ["github_stars", "setup_time_minutes"]
        for field in int_fields:
            if field in resource and not isinstance(resource[field], int):
                raise ValidationError(f"Field '{field}' must be an integer")

    def _validate_field_values(
        self, resource: Dict[str, Any], resource_id: str
    ) -> None:
        """Validate field values against allowed options."""

        # Domain validation
        domains = resource.get("domain", [])
        if len(domains) > 2:
            raise ValidationError("Maximum 2 domains allowed")

        invalid_domains = [d for d in domains if d not in VALID_DOMAINS]
        if invalid_domains:
            raise ValidationError(
                f"Invalid domains: {invalid_domains}. Valid: {VALID_DOMAINS}"
            )

        # Type validation
        if resource.get("type") not in VALID_TYPES:
            raise ValidationError(
                f"Invalid type: {resource.get('type')}. Valid: {VALID_TYPES}"
            )

        # Maturity validation
        if resource.get("maturity") not in VALID_MATURITY:
            raise ValidationError(
                f"Invalid maturity: {resource.get('maturity')}. Valid: {VALID_MATURITY}"
            )

        # Effort validation
        if resource.get("effort") not in VALID_EFFORT:
            raise ValidationError(
                f"Invalid effort: {resource.get('effort')}. Valid: {VALID_EFFORT}"
            )

        # Tags validation
        tags = resource.get("tags", [])
        if len(tags) > 6:
            self.warnings.append(
                f"Resource '{resource_id}': Too many tags ({len(tags)}), recommend max 6"
            )

        # Date validation
        date_fields = ["published", "last_updated"]
        for field in date_fields:
            if field in resource:
                date_value = resource[field]
                # Allow YYYY-MM-DD or YYYY-MM formats
                valid_formats = ["%Y-%m-%d", "%Y-%m"]
                is_valid = False
                for fmt in valid_formats:
                    try:
                        datetime.strptime(date_value, fmt)
                        is_valid = True
                        break
                    except ValueError:
                        continue

                if not is_valid:
                    raise ValidationError(
                        f"Invalid date format for '{field}': {date_value}. Use YYYY-MM-DD or YYYY-MM"
                    )

    def _validate_uniqueness(self, resource: Dict[str, Any], resource_id: str) -> None:
        """Check for duplicate IDs and URLs."""
        # Check duplicate IDs
        if resource_id in self.seen_ids:
            raise ValidationError(f"Duplicate ID: {resource_id}")
        self.seen_ids.add(resource_id)

        # Check duplicate URLs
        url = resource.get("url")
        if url:
            normalized_url = self._normalize_url(url)
            if normalized_url in self.seen_urls:
                raise ValidationError(f"Duplicate URL: {url}")
            self.seen_urls.add(normalized_url)

    def _validate_content_quality(
        self, resource: Dict[str, Any], resource_id: str
    ) -> None:
        """Check content quality and completeness."""

        # Summary length check
        summary = resource.get("summary", "")
        if len(summary) < 50:
            self.warnings.append(
                f"Resource '{resource_id}': Summary too short ({len(summary)} chars), recommend 50+"
            )
        elif len(summary) > 300:
            self.warnings.append(
                f"Resource '{resource_id}': Summary too long ({len(summary)} chars), recommend under 300"
            )

        # Why useful check
        why_useful = resource.get("why_useful", "")
        if len(why_useful) < 30:
            self.warnings.append(
                f"Resource '{resource_id}': 'why_useful' too short, be more specific"
            )

        # Title quality
        title = resource.get("title", "")
        if len(title) > 50:
            self.warnings.append(
                f"Resource '{resource_id}': Title too long, consider shortening"
            )

        # Check for generic descriptions
        generic_phrases = [
            "great tool",
            "awesome",
            "amazing",
            "best",
            "perfect",
            "helps you",
            "makes it easy",
            "simple tool",
        ]

        for phrase in generic_phrases:
            if (
                phrase.lower() in summary.lower()
                or phrase.lower() in why_useful.lower()
            ):
                self.warnings.append(
                    f"Resource '{resource_id}': Avoid generic phrase '{phrase}', be more specific"
                )

    def _validate_url_format(self, resource: Dict[str, Any], resource_id: str) -> None:
        """Validate URL format and accessibility."""
        url = resource.get("url")
        if not url:
            return

        # Basic URL format check
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            raise ValidationError(f"Invalid URL format: {url}")

        # HTTPS preference
        if parsed.scheme != "https":
            self.warnings.append(
                f"Resource '{resource_id}': Consider HTTPS URL if available"
            )

        # GitHub specific validation
        if "github.com" in url:
            if not re.match(r"https://github\.com/[\w\-\.]+/[\w\-\.]+/?$", url):
                self.warnings.append(
                    f"Resource '{resource_id}': GitHub URL should be in format https://github.com/owner/repo"
                )

    def _normalize_url(self, url: str) -> str:
        """Normalize URL for duplicate detection."""
        # Remove trailing slash, convert to lowercase
        normalized = url.lower().rstrip("/")

        # Remove common variations
        normalized = normalized.replace("www.", "")

        return normalized

    def validate_cross_references(self, resources: List[Dict[str, Any]]) -> None:
        """Validate cross-references between resources."""
        all_ids = {r.get("id") for r in resources}

        for resource in resources:
            resource_id = resource.get("id")
            related = resource.get("related", [])

            for related_id in related:
                if related_id not in all_ids:
                    self.errors.append(
                        f"Resource '{resource_id}': Invalid related ID '{related_id}'"
                    )

    def check_url_accessibility(
        self, resources: List[Dict[str, Any]], timeout: int = 10
    ) -> None:
        """Check if URLs are accessible (optional, can be slow)."""
        print("🔍 Checking URL accessibility (this may take a moment)...")

        for resource in resources[:5]:  # Limit to first 5 for speed
            url = resource.get("url")
            resource_id = resource.get("id")

            if not url:
                continue

            try:
                response = requests.head(url, timeout=timeout, allow_redirects=True)
                if response.status_code >= 400:
                    self.warnings.append(
                        f"Resource '{resource_id}': URL returned {response.status_code}"
                    )
            except requests.RequestException as e:
                self.warnings.append(
                    f"Resource '{resource_id}': URL check failed - {str(e)[:50]}"
                )


def load_and_validate_yaml() -> Dict[str, Any]:
    """Load and perform basic YAML validation."""
    yaml_path = Path("data/resources.yaml")

    if not yaml_path.exists():
        raise FileNotFoundError(f"Resources file not found: {yaml_path}")

    try:
        with open(yaml_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise ValidationError(f"Invalid YAML format: {e}")

    if not isinstance(data, dict):
        raise ValidationError("YAML root must be a dictionary")

    if "resources" not in data:
        raise ValidationError("YAML must contain 'resources' key")

    if not isinstance(data["resources"], list):
        raise ValidationError("'resources' must be a list")

    return data


def main():
    """Main validation function."""
    print("🔍 Validating resources.yaml...")

    try:
        # Load YAML
        data = load_and_validate_yaml()
        resources = data["resources"]

        print(f"📊 Found {len(resources)} resources to validate")

        # Initialize validator
        validator = ResourceValidator()

        # Validate each resource
        for i, resource in enumerate(resources):
            validator.validate_resource(resource, i)

        # Validate cross-references
        validator.validate_cross_references(resources)

        # Optional URL accessibility check (uncomment if needed)
        # validator.check_url_accessibility(resources)

        # Report results
        print(f"\n📋 Validation Results:")
        print(f"  ✅ Resources validated: {len(resources)}")
        print(f"  ❌ Errors found: {len(validator.errors)}")
        print(f"  ⚠️  Warnings: {len(validator.warnings)}")

        # Print errors
        if validator.errors:
            print(f"\n❌ Errors (must fix):")
            for error in validator.errors:
                print(f"  • {error}")

        # Print warnings
        if validator.warnings:
            print(f"\n⚠️  Warnings (recommended fixes):")
            for warning in validator.warnings:
                print(f"  • {warning}")

        # Exit code
        if validator.errors:
            print(f"\n💥 Validation failed! Please fix errors above.")
            return 1
        elif validator.warnings:
            print(
                f"\n✅ Validation passed with warnings. Consider addressing warnings above."
            )
            return 0
        else:
            print(f"\n🎉 Perfect! No errors or warnings found.")
            return 0

    except Exception as e:
        print(f"💥 Validation failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
