#!/usr/bin/env python3
"""
Generate README.md from resources.yaml
Maintains the structure while updating dynamic content like tables and stats.
"""

import yaml
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Any

# Emoji mappings for visual indicators
MATURITY_EMOJI = {"Battle-tested": "🟢", "Emerging": "🟡", "Experimental": "🔴"}

EFFORT_EMOJI = {"Low": "⚡", "Medium": "⚖️", "High": "🔥"}

TYPE_EMOJI = {
    "Repo": "📦",
    "Article": "📄",
    "Guide": "📖",
    "Tool": "🔧",
    "Framework": "🏗️",
    "Dataset": "📊",
}


def load_resources() -> Dict[str, Any]:
    """Load and validate resources from YAML file."""
    yaml_path = Path("data/resources.yaml")
    if not yaml_path.exists():
        raise FileNotFoundError(f"Resources file not found: {yaml_path}")

    with open(yaml_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if "resources" not in data:
        raise ValueError("YAML must contain 'resources' key")

    return data


def format_github_link(resource: Dict[str, Any]) -> str:
    """Format GitHub repository link with stars if available."""
    title = resource["title"]
    url = resource["url"]

    # Build the link text
    link_parts = [f"**[{title}]({url})**"]

    # Add metadata line
    meta_parts = []
    if resource.get("github_stars"):
        meta_parts.append(f"⭐ {resource['github_stars']:,}")
    if resource.get("language"):
        meta_parts.append(resource["language"])

    if meta_parts:
        link_parts.append(f"<br/>{' • '.join(meta_parts)}")

    return " ".join(link_parts)


def format_resource_row(resource: Dict[str, Any], compact: bool = True) -> str:
    """Format a resource as a table row."""
    if compact:
        # Compact format for main tables
        maturity_icon = MATURITY_EMOJI.get(resource["maturity"], "❓")
        effort_icon = EFFORT_EMOJI.get(resource["effort"], "❓")

        return (
            f"| {format_github_link(resource)} "
            f"| {maturity_icon} {resource['maturity']} "
            f"| {effort_icon} {resource['effort']} "
            f"| {', '.join(resource.get('use_cases', [])[:2])} "
            f"| {resource['summary'][:80]}{'...' if len(resource['summary']) > 80 else ''} |"
        )
    else:
        # Detailed format
        return (
            f"### {resource['title']}\n"
            + f"- **What it is:** {resource['summary']}\n"
            + f"- **Why it's useful:** {resource['why_useful']}\n"
            + f"- **Setup time:** ~{resource.get('setup_time_minutes', 'N/A')} minutes\n"
            + f"- **Prerequisites:** {', '.join(resource.get('prerequisites', ['None']))}\n"
        )


def group_resources_by_domain(
    resources: List[Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Group resources by their primary domain."""
    grouped = defaultdict(list)

    for resource in resources:
        domains = resource.get("domain", [])
        primary_domain = domains[0] if domains else "Other"
        grouped[primary_domain].append(resource)

    # Sort within each domain by maturity (Battle-tested first) then by title
    maturity_order = {"Battle-tested": 0, "Emerging": 1, "Experimental": 2}

    for domain in grouped:
        grouped[domain].sort(
            key=lambda r: (maturity_order.get(r["maturity"], 3), r["title"].lower())
        )

    return dict(grouped)


def create_domain_section(domain: str, resources: List[Dict[str, Any]]) -> str:
    """Create a markdown section for a domain."""
    domain_titles = {
        "LLMOps-RAG": "🤖 AI/ML Engineering",
        "ML-Engineering": "🧠 ML Engineering",
        "DevOps-SRE": "🔧 DevOps & SRE",
        "Data-Engineering": "📊 Data Engineering",
        "Security": "🔒 Security",
        "Systems-Tools": "🛠️ Systems & Tools",
    }

    section_title = domain_titles.get(domain, f"📁 {domain}")
    resource_count = len(resources)

    # Group by subcategory if we can infer them
    subcategories = group_by_subcategory(resources)

    section = f"\n## {section_title}\n\n"

    for subcategory, subcat_resources in subcategories.items():
        section += f"<details open>\n"
        section += f"<summary><strong>{subcategory}</strong> ({len(subcat_resources)} resources)</summary>\n\n"

        # Table header
        section += "| Resource | Maturity | Effort | Use Case | Quick Summary |\n"
        section += "|----------|----------|---------|----------|---------------|\n"

        # Resource rows
        for resource in subcat_resources:
            section += format_resource_row(resource) + "\n"

        section += "\n</details>\n"

    return section


def group_by_subcategory(
    resources: List[Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Group resources into logical subcategories based on tags and types."""
    subcategories = defaultdict(list)

    for resource in resources:
        tags = resource.get("tags", [])
        resource_type = resource.get("type", "Other")

        # Infer subcategory from tags and context
        if any(tag in tags for tag in ["llm", "rag", "prompts", "evaluation"]):
            subcategories["LLMOps & RAG Systems"].append(resource)
        elif any(tag in tags for tag in ["training", "frameworks", "models"]):
            subcategories["ML Frameworks & Training"].append(resource)
        elif any(tag in tags for tag in ["devops", "infrastructure", "ci-cd"]):
            subcategories["Infrastructure & DevOps"].append(resource)
        elif any(tag in tags for tag in ["sql", "database", "query"]):
            subcategories["SQL & Database Tools"].append(resource)
        elif any(tag in tags for tag in ["documentation", "diagrams", "visualization"]):
            subcategories["Documentation & Visualization"].append(resource)
        else:
            # Default categorization
            subcategories["Tools & Utilities"].append(resource)

    return dict(subcategories)


def generate_quick_wins_section(resources: List[Dict[str, Any]]) -> str:
    """Generate the Quick Wins section with low-effort, high-impact resources."""
    quick_wins = [
        r
        for r in resources
        if r.get("effort") == "Low"
        and r.get("maturity") in ["Battle-tested", "Emerging"]
    ]

    if not quick_wins:
        return ""

    section = "\n## ⚡ Quick Wins\n\n"
    section += "Resources you can implement in under 2 hours:\n\n"
    section += "| Resource | Setup Time | Impact | Use Case |\n"
    section += "|----------|------------|---------|----------|\n"

    for resource in quick_wins[:5]:  # Limit to top 5
        setup_time = f"{resource.get('setup_time_minutes', 'N/A')} min"
        impact = "High" if resource["maturity"] == "Battle-tested" else "Medium"
        use_case = ", ".join(resource.get("use_cases", [])[:2])

        section += f"| [{resource['title']}]({resource['url']}) | {setup_time} | {impact} | {use_case} |\n"

    return section + "\n"


def generate_trending_section(resources: List[Dict[str, Any]]) -> str:
    """Generate trending section with recently added resources."""
    # Sort by added date, take most recent
    recent_resources = sorted(
        resources, key=lambda r: r.get("added", "2020-01-01"), reverse=True
    )[:3]

    section = "\n## 🔥 Trending This Month\n\n"
    section += "Recent additions that are gaining traction:\n\n"

    for resource in recent_resources:
        section += f"- **[{resource['title']}]({resource['url']})** - {resource['summary'].split('.')[0]}\n"

    return section + "\n"


def calculate_stats(resources: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate repository statistics."""
    total_resources = len(resources)

    # Count by domain
    domain_counts = Counter()
    for resource in resources:
        for domain in resource.get("domain", []):
            domain_counts[domain] += 1

    # Count by maturity
    maturity_counts = Counter(r.get("maturity", "Unknown") for r in resources)

    # Average GitHub stars
    stars = [r.get("github_stars", 0) for r in resources if r.get("github_stars")]
    avg_stars = sum(stars) / len(stars) if stars else 0

    # All unique tags
    all_tags = []
    for resource in resources:
        all_tags.extend(resource.get("tags", []))

    return {
        "total_resources": total_resources,
        "domains_covered": len(domain_counts),
        "avg_stars": avg_stars,
        "tag_counts": Counter(all_tags),
        "maturity_counts": maturity_counts,
        "last_updated": datetime.now().strftime("%B %Y"),
    }


def generate_stats_section(stats: Dict[str, Any]) -> str:
    """Generate the repository stats section."""
    section = "\n## 📈 Repository Stats\n\n"
    section += f"- **Total Resources:** {stats['total_resources']}\n"
    section += f"- **Domains Covered:** {stats['domains_covered']}\n"
    section += (
        f"- **Average GitHub Stars:** {stats['avg_stars']:,.1f}k\n"
        if stats["avg_stars"] > 1000
        else f"- **Average GitHub Stars:** {stats['avg_stars']:,.0f}\n"
    )
    section += f"- **Last Updated:** {stats['last_updated']}\n"
    section += "- **Contributors:** 1\n\n"

    return section


def generate_tag_cloud(stats: Dict[str, Any]) -> str:
    """Generate tag cloud section."""
    top_tags = stats["tag_counts"].most_common(15)

    section = "\n## 🏷️ Tag Cloud\n\n"
    tag_list = " ".join([f"`{tag}`" for tag, _ in top_tags])
    section += tag_list + "\n"

    return section


def update_readme_template(
    resources: List[Dict[str, Any]], stats: Dict[str, Any]
) -> str:
    """Generate the complete README.md content."""

    # Header with badges
    readme_content = f"""# Engineering Arsenal 🛠️

> A battle-tested collection of tools, resources, and knowledge that actually moved the needle in real engineering projects. Each entry includes practical metadata, honest assessments, and concrete use cases.

[![Resources](https://img.shields.io/badge/Resources-{stats['total_resources']}-blue)](README.md) [![Domains](https://img.shields.io/badge/Domains-{stats['domains_covered']}-green)](README.md) [![Contributors](https://img.shields.io/badge/Contributors-1-orange)](README.md) [![Last Updated](https://img.shields.io/badge/Updated-{stats['last_updated'].replace(' ', '%20')}-red)](README.md)

## 🎯 Quick Navigation

| 🤖 **AI/ML** | 🔧 **DevOps/SRE** | 📊 **Data Eng** | 🏗️ **Systems** | 🔒 **Security** | 🎓 **Learning** |
|-------------|------------------|-----------------|----------------|-----------------|-----------------|"""

    # Count resources per domain
    domain_counts = {}
    grouped = group_resources_by_domain(resources)
    for domain, domain_resources in grouped.items():
        domain_counts[domain] = len(domain_resources)

    # Navigation table row
    nav_links = []
    nav_counts = []

    domain_mapping = {
        "LLMOps-RAG": ("AI/ML", "#-aiml-engineering"),
        "DevOps-SRE": ("DevOps", "#-devops--sre"),
        "Data-Engineering": ("Data", "#-data-engineering"),
        "Systems-Tools": ("Systems", "#-systems--tools"),
        "Security": ("Security", "#-security"),
        "ML-Engineering": ("Learning", "#-ml-engineering"),
    }

    for domain, (name, link) in domain_mapping.items():
        count = domain_counts.get(domain, 0)
        nav_links.append(f"[Jump to {name}]({link})")
        nav_counts.append(f"{count} resources")

    readme_content += f"""
| {' | '.join(nav_links)} |
| {' | '.join(nav_counts)} |

**🏷️ Filter by:** [⚡ Quick Wins](#quick-wins) • [🟢 Production Ready](#production-ready) • [🟡 Emerging](#emerging) • [🔥 Trending](#trending)

---
"""

    # Generate domain sections
    for domain, domain_resources in grouped.items():
        readme_content += create_domain_section(domain, domain_resources)

    # Add special sections
    readme_content += generate_trending_section(resources)
    readme_content += generate_quick_wins_section(resources)

    # Contributing section
    readme_content += """
## 🤝 Contributing

Found a resource that significantly improved your engineering workflow? 

**Quick Add:** Create an issue with the URL and a brief "why it's useful" note.

**Detailed Add:** Follow the [contribution template](.github/ISSUE_TEMPLATE/add-resource.md).

**Quality Standards:**
- Must have used it successfully in a real project
- Should solve a concrete engineering problem
- Include honest assessment of effort/complexity

---
"""

    # Stats and tag cloud
    readme_content += generate_stats_section(stats)
    readme_content += generate_tag_cloud(stats)

    # Footer
    readme_content += f"""
---

## 📄 License

Content and curation by [@yourusername](https://github.com/yourusername). Resource descriptions under CC BY 4.0. Code examples under MIT.

---

*This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning. No affiliate links, no sponsored content—just honest recommendations.*

<!-- Auto-generated from data/resources.yaml on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -->
"""

    return readme_content


def main():
    """Main execution function."""
    try:
        print("🔄 Loading resources from YAML...")
        data = load_resources()
        resources = data["resources"]

        print(f"📊 Processing {len(resources)} resources...")
        stats = calculate_stats(resources)

        print("📝 Generating README.md...")
        readme_content = update_readme_template(resources, stats)

        # Write to README.md
        readme_path = Path("README.md")
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(readme_content)

        print(
            f"✅ Successfully generated README.md with {stats['total_resources']} resources!"
        )
        print(
            f"📈 Stats: {stats['domains_covered']} domains, {len(stats['tag_counts'])} unique tags"
        )

    except Exception as e:
        print(f"❌ Error generating README: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
