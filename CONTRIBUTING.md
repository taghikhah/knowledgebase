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
  domain: [Primary-Domain, Secondary-Domain] # Max 2
  type: Repo # Repo | Article | Guide | Tool | Framework | Dataset
  maturity: Emerging # Battle-tested | Emerging | Experimental
  effort: Medium # Low (<2hrs) | Medium (weekend) | High (weeks)
  tags: [tag1, tag2, tag3, tag4, tag5] # Max 6, lowercase with hyphens
  source_owner: github-username-or-org # If applicable
  license: MIT # If known
  github_stars: 1200 # If GitHub repo
  language: Python # Primary language or N/A
  added: 2024-09-22 # Date added
  last_checked: 2024-09-22 # Last verification date
  last_updated: 2024-09 # Last update from source (YYYY-MM)
  summary: >
    2-3 sentence factual description of what this resource is and what it does.
    Focus on capabilities and core functionality.
  why_useful: >
    1-2 sentences explaining practical value. Use concrete examples like
    "saves 3 hours of debugging" or "prevents common production issues."
  good_for: [learning, production, POCs] # Target use cases
  setup_time_minutes: 60 # Realistic estimate
  prerequisites: [Python, Docker, basic-ML] # What you need to know
  use_cases: [specific, concrete, examples, of, usage]
  related: [other-resource-ids] # IDs from this file
```

## 🏷️ Domain Classification

Choose **1-2 domains maximum**:

| Domain             | Description                             | Examples                                          |
| ------------------ | --------------------------------------- | ------------------------------------------------- |
| `LLMOps-RAG`       | LLM operations, RAG, prompt engineering | Testing frameworks, evaluation tools, RAG systems |
| `ML-Engineering`   | Traditional ML, training, frameworks    | Training tools, feature stores, model serving     |
| `DevOps-SRE`       | Infrastructure, monitoring, deployment  | CI/CD, monitoring, infrastructure as code         |
| `Data-Engineering` | Pipelines, processing, storage          | ETL tools, data quality, stream processing        |
| `Security`         | Application & infrastructure security   | Scanning tools, authentication, compliance        |
| `Systems-Tools`    | Development tools, utilities            | Diagrams, CLI tools, development utilities        |

## 🔄 Maturity Assessment Guidelines

Be honest about maturity levels:

- **Battle-tested** 🟢: Widely adopted in production, stable APIs, strong community

  - Examples: Docker, Kubernetes, React, PostgreSQL
  - Indicators: 1000+ GitHub stars, enterprise adoption, stable releases

- **Emerging** 🟡: Gaining traction, active development, some production use

  - Examples: New frameworks getting adoption, tools with growing communities
  - Indicators: 100-1000 stars, regular releases, growing documentation

- **Experimental** 🔴: Early stage, research projects, proof of concepts
  - Examples: Academic research, early prototypes, bleeding-edge tools
  - Indicators: <100 stars, irregular updates, limited documentation

## ⚡ Effort Level Guidelines

- **Low** (⚡): Can implement/use within 2 hours
  - Copy-paste examples, simple CLI tools, reading material
- **Medium** (⚖️): Weekend project, requires some learning
  - New frameworks, complex configurations, moderate learning curve
- **High** (🔥): Major time investment, weeks to implement
  - Complete system overhauls, steep learning curves, enterprise deployments

## 🏷️ Tagging Best Practices

Use **4-6 tags maximum**, follow these patterns:

**Technology tags**: `python`, `docker`, `kubernetes`, `sql`, `typescript`
**Purpose tags**: `testing`, `monitoring`, `documentation`, `automation`
**Domain tags**: `mlops`, `devops`, `rag`, `cicd`, `security`
**Pattern tags**: `patterns`, `best-practices`, `case-studies`, `templates`

Use lowercase with hyphens: `machine-learning`, `ci-cd`, `natural-language`

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

## ❓ Questions?

- Create a [discussion](../../discussions) for general questions
- Create an [issue](../../issues) for bugs or specific resource suggestions
- Mention `@yourusername` in comments for urgent reviews

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this repository (MIT for code, CC BY 4.0 for content).

---

_Thanks for helping build a valuable resource for the engineering community!_
