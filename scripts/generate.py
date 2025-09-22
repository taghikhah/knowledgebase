#!/usr/bin/env python3
"""
Generate README.md from resources.yaml - Polished Version 1
Maintains the clean table layout with small visual improvements.
"""

import yaml
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Any

# Consistent emoji mappings
MATURITY_EMOJI = {"Battle-tested": "🟢", "Emerging": "🟡", "Experimental": "🔴"}

EFFORT_EMOJI = {"Low": "⚡", "Medium": "⚖️", "High": "🔥"}


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


def format_resource_row(resource: Dict[str, Any]) -> str:
    """Format a resource as a table row with improved styling."""

    # Enhanced title with bold formatting and metadata
    github_info = ""
    if resource.get("github_stars"):
        github_info = f"<br/>⭐ {resource['github_stars']:,}"
        if resource.get("language"):
            github_info += f" • {resource['language']}"

    title_cell = f"**[{resource['title']}]({resource['url']})**{github_info}"

    # Consistent emoji usage
    maturity_cell = (
        f"{MATURITY_EMOJI.get(resource['maturity'], '❓')} {resource['maturity']}"
    )
    effort_cell = f"{EFFORT_EMOJI.get(resource['effort'], '❓')} {resource['effort']}"

    # Clean use cases (limit to first 2-3 for readability)
    use_cases = ", ".join(resource.get("use_cases", [])[:3])

    # Summary with proper truncation
    summary = resource["summary"]
    if len(summary) > 120:
        summary = summary[:117] + "..."

    return (
        f"| {title_cell} | {maturity_cell} | {effort_cell} | {use_cases} | {summary} |"
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
            key=lambda r: (
                maturity_order.get(r["maturity"], 3),
                -r.get("github_stars", 0),  # Higher stars first
                r["title"].lower(),
            )
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

    section = f"\n### {section_title}\n\n"

    for subcategory, subcat_resources in subcategories.items():
        section += f"<details open>\n"
        section += f"<summary><strong>{subcategory}</strong> ({len(subcat_resources)} resources)</summary>\n\n"

        # Table header
        section += "| Resource | Maturity | Effort | Use Case | Quick Summary |\n"
        section += "|----------|:--------:|:------:|----------|---------------|\n"

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
        tags = [tag.lower() for tag in resource.get("tags", [])]

        # Improved categorization logic
        if any(tag in tags for tag in ["llmops", "rag", "prompts", "evaluation"]):
            subcategories["🎯 LLMOps & RAG Systems"].append(resource)
        elif any(
            tag in tags for tag in ["training", "frameworks", "models", "apple-silicon"]
        ):
            subcategories["🧠 ML Frameworks & Training"].append(resource)
        elif any(
            tag in tags for tag in ["devops", "infrastructure", "ci-cd", "deployment"]
        ):
            subcategories["🏗️ Infrastructure & DevOps"].append(resource)
        elif any(
            tag in tags
            for tag in ["testing", "performance", "load-testing", "monitoring"]
        ):
            subcategories["📈 Testing & Performance"].append(resource)
        elif any(tag in tags for tag in ["sql", "database", "query"]):
            subcategories["🗄️ SQL & Database Tools"].append(resource)
        elif any(tag in tags for tag in ["documentation", "diagrams", "visualization"]):
            subcategories["📋 Documentation & Visualization"].append(resource)
        elif any(tag in tags for tag in ["security", "scanning", "auth"]):
            subcategories["🔒 Security & Compliance"].append(resource)
        else:
            subcategories["🛠️ Tools & Utilities"].append(resource)

    return dict(subcategories)


def generate_quick_navigation(
    grouped_resources: Dict[str, List[Dict[str, Any]]],
) -> str:
    """Generate the enhanced quick navigation section."""
    domain_info = {
        "LLMOps-RAG": ("🤖 **AI/ML**", "aiml-engineering"),
        "ML-Engineering": ("🧠 **ML Engineering**", "ml-engineering"),
        "DevOps-SRE": ("🔧 **DevOps/SRE**", "devops--sre"),
        "Data-Engineering": ("📊 **Data Eng**", "data-engineering"),
        "Security": ("🔒 **Security**", "security"),
        "Systems-Tools": ("🛠️ **Systems**", "systems--tools"),
    }

    nav_section = '\n## 🎯 Quick Navigation\n\n<div align="center">\n\n'

    # Create table header
    headers = []
    links = []
    counts = []

    for domain, resources in grouped_resources.items():
        if domain in domain_info:
            emoji_title, anchor = domain_info[domain]
            headers.append(emoji_title)
            links.append(
                f"[Jump to {emoji_title.replace('**', '').replace('🤖 ', '').replace('🧠 ', '').replace('🔧 ', '').replace('📊 ', '').replace('🔒 ', '').replace('🛠️ ', '')}](#{anchor})"
            )
            counts.append(f"**{len(resources)} resources**")

    # Build the navigation table
    nav_section += "| " + " | ".join(headers) + " |\n"
    nav_section += "|" + ":------------:|" * len(headers) + "\n"
    nav_section += "| " + " | ".join(links) + " |\n"
    nav_section += "| " + " | ".join(counts) + " |\n"

    nav_section += "\n</div>\n\n"
    nav_section += "**🏷️ Filter by:** [⚡ Quick Wins](#quick-wins) • [🟢 Production Ready](#production-ready) • [🟡 Emerging](#emerging) • [🔥 Trending](#trending)\n"

    return nav_section


def generate_quick_wins_section(resources: List[Dict[str, Any]]) -> str:
    """Generate the Quick Wins section."""
    quick_wins = [
        r
        for r in resources
        if r.get("effort") == "Low"
        and r.get("maturity") in ["Battle-tested", "Emerging"]
    ]

    if not quick_wins:
        return ""

    # Sort by impact (battle-tested first, then by stars)
    quick_wins.sort(
        key=lambda r: (
            0 if r["maturity"] == "Battle-tested" else 1,
            -r.get("github_stars", 0),
        )
    )

    section = "\n## ⚡ Quick Wins\n\n"
    section += "Resources you can implement in under 2 hours:\n\n"
    section += "| Resource | Setup Time | Impact | Use Case |\n"
    section += "|----------|:----------:|:------:|----------|\n"

    for resource in quick_wins[:4]:  # Limit to top 4
        setup_time = f"{resource.get('setup_time_minutes', 'N/A')} min"
        impact = "High" if resource["maturity"] == "Battle-tested" else "Medium"
        use_case = ", ".join(resource.get("use_cases", [])[:2])

        section += f"| [**{resource['title']}**]({resource['url']}) | {setup_time} | {impact} | {use_case} |\n"

    return section + "\n"


def generate_trending_section(resources: List[Dict[str, Any]]) -> str:
    """Generate trending section with recently added resources."""
    # Sort by added date, take most recent
    recent_resources = sorted(
        resources,
        key=lambda r: (r.get("added", "2020-01-01"), r.get("github_stars", 0)),
        reverse=True,
    )[:3]

    section = "\n## 🔥 Trending This Month\n\n"
    section += "Recent additions that are gaining traction:\n\n"

    for resource in recent_resources:
        summary_line = resource["summary"].split(".")[0] + "."
        section += f"• **[{resource['title']}]({resource['url']})** - {summary_line}\n"

    return section + "\n"


def calculate_stats(resources: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate repository statistics."""
    total_resources = len(resources)

    # Count by domain
    domain_counts = Counter()
    for resource in resources:
        for domain in resource.get("domain", []):
            domain_counts[domain] += 1

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
        "last_updated": datetime.now().strftime("%B %Y"),
    }


def generate_stats_section(stats: Dict[str, Any]) -> str:
    """Generate the repository stats section."""
    section = "\n## 📊 Repository Stats\n\n"
    section += f"• **Total Resources:** {stats['total_resources']}\n"
    section += f"• **Domains Covered:** {stats['domains_covered']}\n"
    # section += (
    #     f"• **Average GitHub Stars:** {stats['avg_stars']:,.1f}k\n"
    #     if stats["avg_stars"] > 1000
    #     else f"• **Average GitHub Stars:** {stats['avg_stars']:,.0f}\n"
    # )
    section += f"• **Last Updated:** {stats['last_updated']}\n"
    section += f"• **Contributors:** 1\n\n"

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
    grouped = group_resources_by_domain(resources)

    # Header with improved badges
    readme_content = f"""# Engineering Arsenal 🛠️

A curated, enterprise-grade collection of links, repos, and notes that actually helped me build real systems (ML/AI, LLMOps, DevOps, Data Eng, SRE, Security). Each entry includes structured metadata, honest assessments, and why it's useful in practice.

<div align="center">

![Resources](https://img.shields.io/badge/Resources-{stats['total_resources']}-blue) ![Domains](https://img.shields.io/badge/Domains-{stats['domains_covered']}-green) ![Contributors](https://img.shields.io/badge/Contributors-1-orange) ![Last Updated](https://img.shields.io/badge/Updated-{stats['last_updated'].replace(' ', '%20')}-red)

</div>

{generate_quick_navigation(grouped)}

---
"""

    # Generate domain sections
    for domain, domain_resources in grouped.items():
        readme_content += create_domain_section(domain, domain_resources)
        readme_content += "\n---\n"

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

## 🎖️ Recognition

This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning.

**No affiliate links • No sponsored content • Just honest recommendations**

---

## 📄 License

Content and curation by [@taghikhah](https://github.com/taghikhah). Resource descriptions under CC BY 4.0. Code examples under MIT.

⭐ **Star this repo** if you find it valuable • **[Share feedback](../../discussions)**

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

        print("📝 Generating polished README.md...")
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
