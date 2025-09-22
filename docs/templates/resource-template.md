# Resource Entry Template

Use this template when manually adding resources to `data/resources.yaml`:

```yaml
- id: descriptive-slug-name
  title: Official Resource Name
  url: https://exact-resource-url.com
  domain: [Primary-Domain, Secondary-Domain] # Maximum 2 domains
  type: Repo # Repo | Article | Guide | Tool | Framework | Dataset | Spec
  maturity: Emerging # Battle-tested | Emerging | Experimental
  effort: Medium # Low | Medium | High
  tags: [tag1, tag2, tag3, tag4] # 4-6 tags maximum, lowercase-with-hyphens
  source_owner: github-username-or-org # If applicable (GitHub repos)
  license: MIT # If known
  github_stars: 1500 # Current count if GitHub repo
  language: Python # Primary language or N/A
  added: 2024-09-22 # Date added (YYYY-MM-DD)
  last_checked: 2024-09-22 # Last verification date (YYYY-MM-DD)
  last_updated: 2024-09 # Last update from source (YYYY-MM)
  summary: >
    Factual 2-3 sentence description of what this resource IS and what it does.
    Focus on technical capabilities and core functionality without promotional language.
  why_useful: >
    Practical explanation of WHY this matters to engineers. Include concrete benefits,
    specific problems it solves, or quantified value like time savings or risk reduction.
  good_for: [production, learning, POCs] # Target use cases
  setup_time_minutes: 90 # Realistic time estimate for basic setup/usage
  prerequisites: [Python, Docker, basic-knowledge] # Required skills/tools
  use_cases: [specific, concrete, examples, of, real, usage] # 4-6 specific scenarios
  related: [other-resource-ids-from-this-file] # Connect related resources
```

## Field Descriptions

### Required Fields

- **id**: Unique identifier, lowercase with hyphens (e.g., `promptfoo`, `mlx-apple`)
- **title**: Official name as shown on the resource itself
- **url**: Exact URL to the resource (prefer HTTPS when available)
- **domain**: 1-2 domains from the approved list
- **type**: Primary type of resource
- **maturity**: Honest assessment of adoption and stability
- **effort**: Realistic time investment for basic usage
- **tags**: 4-6 descriptive tags, lowercase with hyphens
- **added**: Date you're adding this entry
- **summary**: What the resource IS (factual, technical)
- **why_useful**: Why engineers should care (practical benefits)
- **good_for**: Primary use case scenarios

### Optional Fields

- **source_owner**: GitHub username/org for repositories
- **license**: Software license if known
- **github_stars**: Current star count (auto-updated weekly)
- **language**: Primary programming language
- **last_checked**: When you last verified the resource works
- **last_updated**: When the resource was last updated (from source)
- **setup_time_minutes**: Realistic setup/learning time
- **prerequisites**: Required knowledge or tools
- **use_cases**: Specific scenarios where this applies
- **related**: IDs of related resources for cross-referencing

## Domain Categories

| Domain             | Description                             | Examples                                  |
| ------------------ | --------------------------------------- | ----------------------------------------- |
| `LLMOps-RAG`       | LLM operations, RAG, prompt engineering | Testing frameworks, evaluation tools      |
| `ML-Engineering`   | Traditional ML, training, serving       | Frameworks, feature stores, model serving |
| `DevOps-SRE`       | Infrastructure, monitoring, deployment  | CI/CD tools, monitoring, IaC              |
| `Data-Engineering` | Pipelines, processing, storage          | ETL tools, data quality, streaming        |
| `Security`         | Application & infrastructure security   | Scanning tools, auth, compliance          |
| `Systems-Tools`    | Development utilities, documentation    | Diagram tools, CLI utilities              |

## Maturity Levels

- **Battle-tested** 🟢: Widely adopted in production, stable APIs, strong community

  - 1000+ GitHub stars OR well-known industry standard
  - Regular maintenance and updates
  - Extensive documentation and examples

- **Emerging** 🟡: Gaining traction, active development, some production use

  - 100-1000 stars OR growing adoption in specific niches
  - Active development with regular releases
  - Good documentation, growing community

- **Experimental** 🔴: Early stage, research projects, proof of concepts
  - <100 stars OR very new/niche
  - Irregular updates or early development
  - Limited documentation or examples

## Effort Levels

- **Low** ⚡: Can implement/use within 2 hours

  - Copy-paste examples work immediately
  - Simple CLI tools with clear instructions
  - Reading material or reference guides

- **Medium** ⚖️: Weekend project, requires some learning

  - New frameworks requiring configuration
  - Tools with moderate learning curve
  - Integration projects

- **High** 🔥: Major time investment, weeks to implement properly
  - Complete system overhauls
  - Steep learning curves
  - Enterprise-level deployments

## Writing Guidelines

### Summary (What it IS):

✅ **Good**: "Open-source testing framework for LLM prompts with CI/CD integration, supporting multiple providers and automated evaluation metrics."

❌ **Bad**: "This is a great tool that helps you test your prompts and make sure they work well."

### Why Useful (Why it MATTERS):

✅ **Good**: "Prevents prompt regression in production, enables systematic comparison of providers, saves 2-3 hours per evaluation cycle."

❌ **Bad**: "Really helpful tool that makes testing easier and is great for developers."

### Tags:

- Use lowercase with hyphens: `machine-learning`, `ci-cd`, `natural-language`
- Mix technology, function, and domain tags
- 4-6 tags maximum for best discoverability

## Validation

After adding your entry:

1. Run validation: `python scripts/validate.py`
2. Fix any errors or warnings
3. Generate README: `python scripts/generate.py`
4. Commit changes with descriptive message

## Examples

See the existing entries in `data/resources.yaml` for real examples of well-formatted entries.
