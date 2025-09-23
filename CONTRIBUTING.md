# Contributing to Engineering Arsenal

Thanks for your interest in contributing! This repository maintains high-quality, battle-tested resources that have proven useful in real engineering projects.

## 🎯 Quality Standards

Only add resources that meet **ALL** of these criteria:

- ✅ **Battle-tested**: You (or a trusted colleague) have used it successfully in a real project
- ✅ **Solves real problems**: Addresses concrete engineering challenges, not just theoretical concepts
- ✅ **Actively maintained**: Shows recent activity OR is foundational/reference material
- ✅ **Accessible**: Core functionality available without paywalls (freemium OK)
- ✅ **Well-documented**: Clear setup instructions and usage examples

## 🚀 Quick Contribution Methods

### Method 1: Create an Issue (Easiest)

[Create a new resource suggestion issue](../../issues/new/choose) with:

- Resource URL
- 2-3 sentences on what it is
- 1-2 sentences on why it's useful
- How you've used it successfully

### Method 2: Direct PR (For experienced contributors)

1. Fork the repository
2. Add entry to `data/resources.yaml`
3. Run `python scripts/generate.py` to update README
4. Submit PR with template below

## 📋 Resource Entry Template

When adding to `data/resources.yaml`, use this structure:

```yaml
- id: unique-slug-name
  title: Display Name
  url: https://example.com/resource
  domains: [AI-Engineering] # Required: 1-3 domains from controlled list
  type: Repo # Required: Repo | Article | Guide | Tool | Framework | Dataset
  maturity: Emerging # Required: Battle-tested | Adopted | Emerging | Experimental
  tags: [tag1, tag2, tag3] # Required: max 6, from controlled vocabulary in data/tags.txt
  github_stars: 1200 # Optional: for GitHub repos
  published: '2024-01' # Optional: YYYY, YYYY-MM, or YYYY-MM-DD
  last_updated: '2024-09' # Optional: when resource was last updated
  added: '2024-09-23' # Optional: when added to this knowledgebase
  summary: > # Required: concise description
    2-3 sentence factual description of what this resource is and what it does.
    Focus on capabilities and core functionality.
  why_useful: > # Optional: why it's valuable
    1-2 sentences explaining practical value. Use concrete examples like
    "saves 3 hours of debugging" or "prevents common production issues."
  good_for: [learning, production, POCs] # Required: from controlled vocabulary
  prerequisites: [Python, Docker, basic-ML] # Optional: what you need to know
  use_cases: [specific, concrete, examples, of, usage] # Optional: concrete examples
  related: [other-resource-ids] # Optional: cross-references by ID
```

## 🏷️ Domain Classification

Choose **1-3 domains maximum** from the new taxonomy:

| Domain                | Description                                          | Examples                                     |
| --------------------- | ---------------------------------------------------- | -------------------------------------------- |
| `AI-Engineering`      | Agents/MCP, RAG & knowledge systems, testing & eval | Agent systems, RAG, evaluation, ML training |
| `Platform-Engineering` | Infrastructure, observability, container platforms  | Monitoring, IaC, containers, CI/CD          |
| `Data-Engineering`    | Discovery, query & storage, pipelines & analytics   | Data catalogs, SQL tools, ETL, analytics    |
| `Security`            | Supply chain, runtime security, auth & compliance   | Vulnerability scanning, secrets, compliance |
| `Developer-Tools`     | Code quality, browser tools, CLI/productivity       | Formatters, browser automation, utilities    |
| `Other`               | Resources that don't fit other categories           | General tools and utilities                  |

## 🔄 Maturity Assessment Guidelines

Be honest about maturity levels:

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

## 🎯 Good For Categories

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

## 🏷️ Tagging Best Practices

Use **3-6 tags maximum** from the controlled vocabulary in `data/tags.txt`:

**AI-Engineering**: `agents`, `mcp`, `rag`, `graph-rag`, `evaluation`, `training`, `architecture`
**Platform-Engineering**: `performance`, `monitoring`, `infrastructure`, `containers`, `ci-cd`, `documentation`
**Data-Engineering**: `datasets`, `sql`, `pipelines`, `analytics`, `governance`, `discovery`
**Security**: `vulnerability-scanning`, `secrets`, `compliance`, `supply-chain`
**Developer-Tools**: `code-formatting`, `browser-automation`, `productivity`, `cli`
**Cross-cutting**: `patterns`, `open-source`, `frameworks`, `learning`, `battle-tested`

All tags must be from the controlled vocabulary. To add new tags, update `data/tags.txt` with justification.

## ✅ PR Review Process

Your PR will be reviewed for:

1. **Relevance**: Fits repository scope and quality standards
2. **Accuracy**: Metadata matches actual resource
3. **Completeness**: All required fields filled correctly
4. **Uniqueness**: Not duplicate or very similar to existing entries
5. **Value**: Clear practical benefit explained

## 🔗 Avoiding Duplicates

Before submitting, check for similar resources:

- Search existing entries in `data/resources.yaml`
- Look for tools solving the same problem
- Consider if your resource adds unique value

If similar resources exist, explain in your PR why this one is different/better.

## 📝 Writing Guidelines

### Summary Writing

- Start with what it IS, not what it does
- Use present tense, active voice
- Include key technical details (languages, platforms)
- 2-3 sentences maximum

**Good**: "Open-source testing framework for LLM prompts with CI/CD integration, supporting multiple providers and evaluation metrics."

**Bad**: "This is a great tool that helps you test your prompts and it's really useful for making sure your LLM apps work well."

### Why Useful Writing

- Focus on practical benefits and concrete outcomes
- Mention specific problems it solves
- Include ROI or time savings when possible
- Avoid generic praise

**Good**: "Prevents prompt regression in production, enables systematic comparison of providers, saves 2-3 hours per evaluation cycle."

**Bad**: "Really helpful tool that makes things easier and is great for testing."

## 🚫 What NOT to Submit

- **Tutorials without code**: Blog posts that don't provide actionable resources
- **Commercial tools**: Paid-only services (freemium with substantial free tier OK)
- **Inactive projects**: No updates in 2+ years unless foundational
- **Duplicate functionality**: Very similar to existing entries without clear differentiation
- **Personal projects**: Your own work (get independent validation first)
- **Promotional content**: Resources that are primarily marketing

## 🤖 Automated Updates

This repository uses GitHub Actions to:

- Validate YAML schema on PRs
- Update GitHub star counts weekly
- Check for broken links monthly
- Regenerate README tables from YAML

Don't manually edit README.md tables - they'll be overwritten!

## 📋 Schema Validation

All resources are validated against `data/schema.json`. The system enforces:

- **Required fields**: id, title, url, domains, type, maturity, tags, summary, good_for
- **Controlled vocabularies**: domains, types, maturity levels, good_for values
- **Tag validation**: All tags must exist in `data/tags.txt`
- **Multi-domain support**: Resources can belong to multiple domains (max 3)
- **Date validation**: Flexible date formats (YYYY, YYYY-MM, YYYY-MM-DD)

## ❓ Questions?

- Create a [discussion](../../discussions) for general questions
- Create an [issue](../../issues) for bugs or specific resource suggestions
- Mention `@yourusername` in comments for urgent reviews

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this repository (MIT for code, CC BY 4.0 for content).

---

_Thanks for helping build a valuable resource for the engineering community!_
