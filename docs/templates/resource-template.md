# Resource Entry Template

Use this template when manually adding resources to `data/resources.yaml`:

```yaml
- id: descriptive-slug-name
  title: Official Resource Name
  url: https://exact-resource-url.com
  domains: [AI-Engineering, Platform-Engineering] # 1-3 domains maximum
  type: Repo # Repo | Article | Guide | Talk | Tool | Framework | Dataset | Spec
  maturity: Emerging # Battle-tested | Adopted | Emerging | Experimental
  tags: [tag1, tag2, tag3, tag4] # 3-6 tags maximum from controlled vocabulary
  github_stars: 1500 # Current count if GitHub repo
  published: '2024-01' # Original publication date (YYYY, YYYY-MM, or YYYY-MM-DD)
  last_updated: '2024-09' # Last significant update (YYYY, YYYY-MM, or YYYY-MM-DD)
  added: '2024-09-23' # Date added to knowledgebase (YYYY-MM-DD)
  summary: >
    Factual 2-3 sentence description of what this resource IS and what it does.
    Focus on technical capabilities and core functionality without promotional language.
  why_useful: >
    Practical explanation of WHY this matters to engineers. Include concrete benefits,
    specific problems it solves, or quantified value like time savings or risk reduction.
  good_for: [production, learning, POCs] # Multiple allowed from controlled vocabulary
  prerequisites: [Python, Docker, basic-knowledge] # Optional: Required skills/tools
  use_cases: [specific, concrete, examples, of, real, usage] # Optional: 4-6 specific scenarios
  related: [other-resource-ids-from-this-file] # Optional: Connect related resources
```

## Field Descriptions

### Required Fields

- **id**: Unique identifier, lowercase with hyphens (e.g., `promptfoo`, `mlx-apple`)
- **title**: Official name as shown on the resource itself
- **url**: Exact URL to the resource (prefer HTTPS when available)
- **domains**: 1-3 domains from the approved list
- **type**: Primary type of resource
- **maturity**: Honest assessment of adoption and stability
- **tags**: 4-6 descriptive tags, lowercase with hyphens
- **published**: When the resource was originally created/published
- **last_updated**: When the resource was last significantly updated
- **added**: Date you're adding this entry
- **summary**: What the resource IS (factual, technical)
- **why_useful**: Why engineers should care (practical benefits)
- **good_for**: Primary use case scenarios

### Optional Fields

- **github_stars**: Current star count (auto-updated weekly)
- **prerequisites**: Required knowledge or tools
- **use_cases**: Specific scenarios where this applies
- **related**: IDs of related resources for cross-referencing

## Domain Categories

| Domain                | Description                                          | Examples                                     |
| --------------------- | ---------------------------------------------------- | -------------------------------------------- |
| `AI-Engineering`      | Agents/MCP, RAG & knowledge systems, testing & eval | Agent systems, RAG, evaluation, ML training |
| `Platform-Engineering` | Infrastructure, observability, container platforms  | Monitoring, IaC, containers, CI/CD          |
| `Data-Engineering`    | Discovery, query & storage, pipelines & analytics   | Data catalogs, SQL tools, ETL, analytics    |
| `Security`            | Supply chain, runtime security, auth & compliance   | Vulnerability scanning, secrets, compliance |
| `Developer-Tools`     | Code quality, browser tools, CLI/productivity       | Formatters, browser automation, utilities    |
| `Other`               | Resources that don't fit other categories           | General tools and utilities                  |

## Maturity Levels

- **Battle-tested** 🛡️: Widely adopted in production, stable APIs, strong community
  - Examples: Docker, Kubernetes, React, PostgreSQL
  - Indicators: 1000+ GitHub stars, enterprise adoption, stable releases

- **Adopted** 🔧: Growing adoption, proven in multiple use cases
  - Examples: Tools gaining enterprise traction, established frameworks
  - Indicators: 500+ stars, multiple production deployments, active community

- **Emerging** 🔧: Gaining traction, active development, some production use
  - Examples: New frameworks getting adoption, tools with growing communities
  - Indicators: 100-1000 stars, regular releases, growing documentation

- **Experimental** 🧪: Early stage, research projects, proof of concepts
  - Examples: Academic research, early prototypes, bleeding-edge tools
  - Indicators: <100 stars, irregular updates, limited documentation

## Good For Categories

Use specific categories from our controlled vocabulary:

- **production**: Ready for production use, proven reliability
- **mlops**: Specifically valuable for ML operations and workflows
- **testing**: Testing, evaluation, and quality assurance
- **evaluation**: Performance measurement and benchmarking
- **prototyping**: Rapid prototyping and proof of concepts
- **learning**: Educational resources and skill development
- **research**: Research projects and academic work
- **experimentation**: Experimental and exploratory work
- **architecture**: System design and architectural decisions
- **strategy**: Strategic planning and decision making
- **POCs**: Proof of concept development
- **documentation**: Documentation and knowledge management
- **discovery**: Resource discovery and exploration
- **integration**: System integration and connectivity
- **monitoring**: Observability and monitoring
- **debugging**: Troubleshooting and debugging
- **performance**: Performance optimization
- **automation**: Workflow automation
- **creative-projects**: Creative and artistic applications

## Writing Guidelines

### Summary (What it IS):

✅ **Good**: "Open-source testing framework for LLM prompts with CI/CD integration, supporting multiple providers and automated evaluation metrics."

❌ **Bad**: "This is a great tool that helps you test your prompts and make sure they work well."

### Why Useful (Why it MATTERS):

✅ **Good**: "Prevents prompt regression in production, enables systematic comparison of providers, saves 2-3 hours per evaluation cycle."

❌ **Bad**: "Really helpful tool that makes testing easier and is great for developers."

### Tags:

- Must be from controlled vocabulary in `data/tags.txt`
- Use 3-6 tags maximum for best discoverability
- Mix technology, function, and domain tags
- Examples: `agents`, `rag`, `containers`, `sql`, `vulnerability-scanning`

## Validation

After adding your entry:

1. Run validation: `python scripts/validate.py`
2. Fix any errors or warnings
3. Generate README: `python scripts/generate.py`
4. Commit changes with descriptive message

## Examples

See the existing entries in `data/resources.yaml` for real examples of well-formatted entries.
