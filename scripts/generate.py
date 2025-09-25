#!/usr/bin/env python3
"""
Generate README.md from resources.yaml - Hybrid Version
Beautiful presentation with advanced categorization algorithm.
"""

import yaml
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Any, Optional

# Consistent emoji mappings (from original)
MATURITY_EMOJI = {
    "Battle-tested": "🛡️",
    "Emerging": "🔧",
    "Experimental": "🧪",
    "Adopted": "🔧",
}

EFFORT_EMOJI = {"Low": "🎯", "Medium": "⚙️", "High": "🚀"}

# New advanced sorting constants
MATURITY_RANK = {"Battle-tested": 0, "Adopted": 1, "Emerging": 2, "Experimental": 3}
GOOD_FOR_PRIORITY = ["production", "mlops", "testing", "evaluation", "prototyping"]


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
        stars = resource["github_stars"]
        if stars >= 1000:
            formatted_stars = (
                f"{stars/1000:.0f}K" if stars % 1000 == 0 else f"{stars/1000:.1f}K"
            )
        else:
            formatted_stars = f"<1K"
        github_info = f"<br/>⭐ {formatted_stars}"

    title_cell = f"**<a href=\"{resource['url']}\" target=\"_blank\">{resource['title']} ↗</a>**{github_info}"

    # Consistent emoji usage (emoji only, no text)
    maturity_cell = MATURITY_EMOJI.get(resource["maturity"], "❓")

    # Use good_for instead of effort since effort was removed
    good_for_list = resource.get("good_for", [])
    if "production" in good_for_list:
        effort_cell = "🎯"  # Production-ready gets priority
    elif any(x in good_for_list for x in ["mlops", "testing"]):
        effort_cell = "⚙️"  # Medium complexity
    else:
        effort_cell = "🚀"  # High learning/research value

    # Clean use cases (limit to first 2-3 for readability)
    use_cases = ", ".join(resource.get("use_cases", [])[:3])

    # Summary with proper truncation
    summary = resource["summary"]
    if len(summary) > 120:
        summary = summary[:117] + "..."

    return (
        f"| {title_cell} | {maturity_cell} | {effort_cell} | {use_cases} | {summary} |"
    )


def parse_date(date_str: Optional[str]) -> datetime:
    """Parse date string in various formats, return datetime for sorting."""
    if not date_str:
        return datetime(1900, 1, 1)  # Very old date for sorting

    # Try different formats
    formats = ["%Y-%m-%d", "%Y-%m", "%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    return datetime(1900, 1, 1)


def get_sort_key(resource: Dict[str, Any]) -> tuple:
    """Generate sort key for stable, signal-first sorting."""
    # Maturity rank (lower is better)
    maturity_rank = MATURITY_RANK.get(resource.get("maturity", ""), 99)

    # Date key (newer first)
    last_updated = resource.get("last_updated")
    published = resource.get("published")
    added = resource.get("added")
    date_key = -int(parse_date(last_updated or published or added).timestamp())

    # GitHub stars (more first)
    github_stars = -(resource.get("github_stars") or 0)

    # Good_for priority (lower index is better)
    good_for = resource.get("good_for", [])
    good_for_key = min(
        [GOOD_FOR_PRIORITY.index(g) for g in good_for if g in GOOD_FOR_PRIORITY]
        or [len(GOOD_FOR_PRIORITY)]
    )

    # Title for alphabetical tiebreak
    title = resource.get("title", "").lower()

    return (maturity_rank, date_key, github_stars, good_for_key, title)


def group_resources_by_domain(
    resources: List[Dict[str, Any]],
) -> Dict[str, List[Dict[str, Any]]]:
    """Group resources by their domains (multi-domain support)."""
    grouped = defaultdict(list)

    for resource in resources:
        domains = resource.get("domains", resource.get("domain", ["Other"]))
        if isinstance(domains, str):
            domains = [domains]

        # Add resource to each of its domains
        for domain in domains:
            grouped[domain].append(resource)

    # Sort within each domain using new advanced sorting
    for domain in grouped:
        grouped[domain].sort(key=get_sort_key)

    return dict(grouped)


def get_domain_description(domain: str) -> str:
    """Get a brief description for each domain section."""
    descriptions = {
        "AI-Engineering": "Agents/MCP, RAG & knowledge systems, testing & eval, training & frameworks, architecture.",
        "Platform-Engineering": "Observability & performance, infra & services (IaC), container platforms, build & delivery, docs/runbooks.",
        "Data-Engineering": "Discovery & governance, query & storage, pipelines & orchestration, analytics & BI.",
        "Security": "Supply chain & vuln mgmt, infra/runtime security, secrets/auth/compliance.",
        "Developer-Tools": "Code quality, browser/web tools, CLI/editors/productivity, creative/specialized.",
    }
    return descriptions.get(domain, "Various engineering tools and resources.")


def create_domain_section(domain: str, resources: List[Dict[str, Any]]) -> str:
    """Create a markdown section for a domain with description."""
    domain_titles = {
        "AI-Engineering": "🤖 AI Engineering",
        "Platform-Engineering": "🏗️ Platform Engineering",
        "Data-Engineering": "📊 Data Engineering",
        "Security": "🔒 Security",
        "Developer-Tools": "🛠️ Developer Tools",
    }

    section_title = domain_titles.get(domain, f"📁 {domain}")
    domain_description = get_domain_description(domain)

    # Group by subcategory using new algorithm
    subcategories = group_by_subcategory(resources, domain)

    section = f"\n### {section_title}\n\n"
    section += f"*{domain_description}*\n\n"

    for subcategory, subcat_resources in subcategories.items():
        section += f"<details>\n"
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
    resources: List[Dict[str, Any]], domain: str
) -> Dict[str, List[Dict[str, Any]]]:
    """Group resources into logical subcategories using new domain-specific rules."""
    subcategories = defaultdict(list)

    for resource in resources:
        tags = [tag.lower() for tag in resource.get("tags", [])]

        if domain == "AI-Engineering":
            if any(tag in tags for tag in ["agents", "mcp", "integration", "protocol"]):
                subcategories["Agent Systems & Integration"].append(resource)
            elif any(
                tag in tags
                for tag in ["rag", "graph-rag", "knowledge-graphs", "retrieval"]
            ):
                subcategories["RAG & Knowledge Systems"].append(resource)
            elif any(tag in tags for tag in ["evaluation", "testing", "prompts"]):
                subcategories["Testing & Evaluation"].append(resource)
            elif any(tag in tags for tag in ["training", "frameworks"]):
                subcategories["Training & Frameworks"].append(resource)
            elif any(
                tag in tags for tag in ["architecture", "case-studies", "patterns"]
            ):
                subcategories["Architecture & Best Practices"].append(resource)
            else:
                subcategories["Core AI Tools"].append(resource)

        elif domain == "Platform-Engineering":
            if any(
                tag in tags for tag in ["performance", "monitoring", "observability"]
            ):
                subcategories["Performance & Observability"].append(resource)
            elif any(
                tag in tags
                for tag in ["infrastructure", "self-hosting", "catalog", "services"]
            ):
                subcategories["Infrastructure & Services"].append(resource)
            elif any(tag in tags for tag in ["containers", "docker", "logs"]):
                subcategories["Container Platforms"].append(resource)
            elif any(
                tag in tags for tag in ["documentation", "diagrams", "architecture"]
            ):
                subcategories["Documentation & Architecture"].append(resource)
            else:
                subcategories["Platform Tools"].append(resource)

        elif domain == "Data-Engineering":
            if any(
                tag in tags
                for tag in ["datasets", "catalog", "discovery", "public-data"]
            ):
                subcategories["Data Discovery & Catalogs"].append(resource)
            elif any(tag in tags for tag in ["sql", "database", "nl2sql"]):
                subcategories["Query & Database Tools"].append(resource)
            elif any(tag in tags for tag in ["pipelines", "etl", "processing"]):
                subcategories["Pipelines & Processing"].append(resource)
            else:
                subcategories["Data Infrastructure"].append(resource)

        elif domain == "Security":
            if any(
                tag in tags
                for tag in ["vulnerability-scanning", "containers", "supply-chain"]
            ):
                subcategories["Vulnerability Management"].append(resource)
            elif any(
                tag in tags
                for tag in ["kubernetes", "admission-controller", "configuration"]
            ):
                subcategories["Infrastructure Security"].append(resource)
            elif any(tag in tags for tag in ["secrets", "auth", "compliance"]):
                subcategories["Access & Compliance"].append(resource)
            else:
                subcategories["Security Tools"].append(resource)

        elif domain == "Developer-Tools":
            if any(
                tag in tags
                for tag in ["code-formatting", "linting", "git-hooks", "pre-commit"]
            ):
                subcategories["Code Quality & Standards"].append(resource)
            elif any(tag in tags for tag in ["browser-automation", "chrome-extension"]):
                subcategories["Browser & Web Tools"].append(resource)
            elif any(tag in tags for tag in ["creative-tools"]):
                subcategories["Creative & Specialized Tools"].append(resource)
            else:
                subcategories["Development Utilities"].append(resource)

        else:
            # Fallback for other domains
            subcategories["Tools & Utilities"].append(resource)

    # Sort each subcategory using advanced sorting
    for subcat_resources in subcategories.values():
        subcat_resources.sort(key=get_sort_key)

    return dict(subcategories)


def generate_quick_navigation(
    grouped_resources: Dict[str, List[Dict[str, Any]]],
) -> str:
    """Generate the quick navigation section with descriptions."""
    domain_info = {
        "AI-Engineering": (
            "🤖 **AI Engineering**",
            "ai-engineering",
            "Agents, RAG & ML systems",
        ),
        "Platform-Engineering": (
            "🏗️ **Platform Engineering**",
            "platform-engineering",
            "Infrastructure & reliability",
        ),
        "Data-Engineering": (
            "📊 **Data Engineering**",
            "data-engineering",
            "Data pipelines & processing",
        ),
        "Security": ("🔒 **Security**", "security", "Security & compliance"),
        "Developer-Tools": (
            "🛠️ **Developer Tools**",
            "developer-tools",
            "Development utilities",
        ),
    }

    nav_section = '\n### Quick Navigation\n\n<div align="center">\n\n'

    # Create table header
    headers = []
    links = []
    counts = []
    descriptions = []

    for domain, resources in grouped_resources.items():
        if domain in domain_info:
            emoji_title, anchor, desc = domain_info[domain]
            headers.append(emoji_title)
            clean_title = (
                emoji_title.replace("**", "")
                .replace("🤖 ", "")
                .replace("🏗️ ", "")
                .replace("📊 ", "")
                .replace("🔒 ", "")
                .replace("🛠️ ", "")
            )
            links.append(f"[Jump to {clean_title}](#{anchor})")
            counts.append(f"**{len(resources)} resources**")
            descriptions.append(f"*{desc}*")

    # Build the navigation table
    nav_section += "| " + " | ".join(headers) + " |\n"
    nav_section += "|" + ":------------:|" * len(headers) + "\n"
    nav_section += "| " + " | ".join(links) + " |\n"
    nav_section += "| " + " | ".join(counts) + " |\n"
    nav_section += "| " + " | ".join(descriptions) + " |\n"

    nav_section += "\n</div>\n\n"

    # Simplified quick access with just the badges
    nav_section += '<div align="center">\n\n'
    nav_section += "[![Quick Wins](https://img.shields.io/badge/⚡_Quick_Wins-Under_2hrs-brightgreen)](#quick-wins) &nbsp;&nbsp;"
    nav_section += "[![Production Ready](https://img.shields.io/badge/🛡️_Production_Ready-Battle_tested-blue)](#production-ready) &nbsp;&nbsp;"
    nav_section += "[![Emerging Tools](https://img.shields.io/badge/🔧_Emerging-Worth_watching-orange)](#emerging-tools)\n\n"
    nav_section += "</div>\n"

    return nav_section


def generate_quick_wins_section(resources: List[Dict[str, Any]]) -> str:
    """Generate the Quick Wins section with one best resource per domain."""
    # Use good_for instead of effort for quick wins
    quick_wins = [
        r
        for r in resources
        if "production" in r.get("good_for", [])
        and r.get("maturity") in ["Battle-tested", "Emerging"]
    ]

    if not quick_wins:
        return ""

    # Group by domain and pick the best resource from each domain
    domain_best = {}
    for resource in quick_wins:
        domains = resource.get("domains", resource.get("domain", ["Other"]))
        if isinstance(domains, str):
            domains = [domains]

        primary_domain = domains[0]

        # If we haven't seen this domain or this resource is better
        if primary_domain not in domain_best:
            domain_best[primary_domain] = resource
        else:
            current_best = domain_best[primary_domain]
            # Better if: battle-tested > emerging, then higher stars
            is_better = (
                resource["maturity"] == "Battle-tested"
                and current_best["maturity"] != "Battle-tested"
            ) or (
                resource["maturity"] == current_best["maturity"]
                and resource.get("github_stars", 0)
                > current_best.get("github_stars", 0)
            )
            if is_better:
                domain_best[primary_domain] = resource

    if not domain_best:
        return ""

    section = "\n## Quick Wins\n\n"
    section += "*Best quick win in each domain - high-impact resources you can implement quickly.*\n\n"
    section += "| Domain | Use Case | Resource |\n"
    section += "|:------|----------|----------|\n"

    # Sort domains for consistent output
    for domain in sorted(domain_best.keys()):
        resource = domain_best[domain]
        use_case = ", ".join(resource.get("use_cases", [])[:2])

        section += f"| {domain} | {use_case} | **<a href=\"{resource['url']}\" target=\"_blank\">{resource['title']} ↗</a>** |\n"

    return section + "\n"


def calculate_basic_stats(resources: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate basic repository statistics."""
    total_resources = len(resources)

    # Count by domain
    domain_counts = Counter()
    for resource in resources:
        domains = resource.get("domains", resource.get("domain", []))
        if isinstance(domains, str):
            domains = [domains]
        for domain in domains:
            domain_counts[domain] += 1

    # All unique tags
    all_tags = []
    for resource in resources:
        all_tags.extend(resource.get("tags", []))

    return {
        "total_resources": total_resources,
        "domains_covered": len(domain_counts),
        "tag_counts": Counter(all_tags),
        "last_updated": datetime.now().strftime("%B %Y"),
    }


def generate_tag_cloud(stats: Dict[str, Any]) -> str:
    """Generate tag cloud section."""
    top_tags = stats["tag_counts"].most_common(12)

    section = "\n## Tag Cloud\n\n"
    tag_list = " ".join([f"`{tag}`" for tag, _ in top_tags])
    section += tag_list + "\n"

    return section


def update_readme_template(
    resources: List[Dict[str, Any]], stats: Dict[str, Any]
) -> str:
    """Generate the complete README.md content."""
    grouped = group_resources_by_domain(resources)

    # Header with improved badges
    readme_content = f"""# Engineering Arsenal (Knowledgebase)

A curated, enterprise-grade collection of links, repos, and notes that actually helped me build real systems (AI, Platform, Data, Security, Developer Tools). Each entry includes structured metadata, honest assessments, and why it's useful in practice.

<div align="center">

![Resources](https://img.shields.io/badge/Resources-{stats['total_resources']}-blue) ![Domains](https://img.shields.io/badge/Domains-{stats['domains_covered']}-green) ![Contributors](https://img.shields.io/badge/Contributors-1-orange) ![Last Updated](https://img.shields.io/badge/Updated-{stats['last_updated'].replace(' ', '%20')}-red)

</div>

{generate_quick_navigation(grouped)}

## Domains

Here you will find tools and resources organized by engineering domain, each with a brief description to help you navigate.

> Please consider following table legends below for maturity and effort indicators.

**Maturity Levels:**
- 🛡️ **Battle-tested** → Production ready, widely adopted in enterprise environments
- 🔧 **Emerging** → Gaining significant traction, active development, worth adopting
- 🧪 **Experimental** → Early stage but promising, good for research and experimentation

**Effort Investment:**
- 🎯 **Production** → Ready for production use, proven value
- ⚙️ **Medium** → Requires moderate setup and learning curve
- 🚀 **Research** → High learning value, experimental or specialized use

---

"""

    # Generate domain sections
    for domain, domain_resources in grouped.items():
        readme_content += create_domain_section(domain, domain_resources)
        readme_content += "\n---\n"

    # Add Quick Wins section
    readme_content += generate_quick_wins_section(resources)

    # Contributing section
    readme_content += """
## Contributing

Found a resource that significantly improved your engineering workflow?

**Quick Add:** Create an issue with the URL and a brief "why it's useful" note.

**Detailed Add:** Follow the [contribution template](.github/ISSUE_TEMPLATE/add-resource.md).

**Quality Standards:**
- Must have used it successfully in a real project
- Should solve a concrete engineering problem
- Include honest assessment of effort/complexity

---
"""

    # Tag cloud only
    readme_content += generate_tag_cloud(stats)

    # Footer
    readme_content += f"""
---

## Recognition

This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning.

**No affiliate links • No sponsored content • Just honest recommendations**

---

## License

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
        stats = calculate_basic_stats(resources)

        print("📝 Generating polished README.md with advanced categorization...")
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

        # Show domain breakdown
        grouped = group_resources_by_domain(resources)
        for domain, domain_resources in grouped.items():
            subcats = group_by_subcategory(domain_resources, domain)
            print(
                f"  🔹 {domain}: {len(domain_resources)} resources in {len(subcats)} subcategories"
            )

    except Exception as e:
        print(f"❌ Error generating README: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
