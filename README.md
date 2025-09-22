# Engineering Arsenal (Knowledgebase)

A curated, enterprise-grade collection of links, repos, and notes that actually helped me build real systems (ML/AI, LLMOps, DevOps, Data Eng, SRE, Security). Each entry includes structured metadata, honest assessments, and why it's useful in practice.

<div align="center">

![Resources](https://img.shields.io/badge/Resources-13-blue) ![Domains](https://img.shields.io/badge/Domains-6-green) ![Contributors](https://img.shields.io/badge/Contributors-1-orange) ![Last Updated](https://img.shields.io/badge/Updated-September%202025-red)

</div>


## Quick Navigation

<div align="center">

| 🤖 **AI/ML** | 🧠 **ML Engineering** | 🔧 **DevOps/SRE** | 📊 **Data Eng** | 🔒 **Security** |
|:------------:|:------------:|:------------:|:------------:|:------------:|
| [Jump to AI/ML](#aiml-engineering) | [Jump to ML Engineering](#ml-engineering) | [Jump to DevOps/SRE](#devops--sre) | [Jump to Data Eng](#data-engineering) | [Jump to Security](#security) |
| **5 resources** | **2 resources** | **3 resources** | **1 resources** | **2 resources** |
| *LLM operations & RAG* | *ML frameworks & training* | *Infrastructure & reliability* | *Data pipelines & processing* | *Security & compliance* |

</div>

<div align="center">

[![Quick Wins](https://img.shields.io/badge/⚡_Quick_Wins-Under_2hrs-brightgreen)](#quick-wins) &nbsp;&nbsp;[![Production Ready](https://img.shields.io/badge/🛡️_Production_Ready-Battle_tested-blue)](#production-ready) &nbsp;&nbsp;[![Emerging Tools](https://img.shields.io/badge/🔧_Emerging-Worth_watching-orange)](#emerging-tools)

</div>


---

## Contents

Here you will find battle-tested tools and resources organized by engineering domain. Each entry includes practical metadata, honest maturity assessments, and concrete use cases to help you select the right solution for your specific needs.

<div align="center">

| **Maturity Levels** | **Time Investment** |
|:------------------|:------------------|
| 🛡️ **Battle-tested** → Production ready, widely adopted in enterprise | 🎯 **Low** → Quick setup and immediate value (<2 hours) |
| 🔧 **Emerging** → Gaining traction, active development, worth adopting | ⚙️ **Medium** → Weekend project with moderate learning curve |
| 🧪 **Experimental** → Early stage but promising, good for research | 🚀 **High** → Major undertaking requiring weeks of investment |

</div>


### 🤖 AI/ML Engineering

*Tools and frameworks for operating Large Language Models in production, including prompt testing, RAG systems, and evaluation frameworks.*

<details open>
<summary><strong>🎯 LLMOps & RAG Systems</strong> (3 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[LLM Patterns: A Comprehensive Guide](https://eugeneyan.com/writing/llm-patterns/)** | 🛡️ | ⚙️ | system architecture, pattern implementation, production design | Comprehensive exploration of practical patterns for building LLM systems, covering evaluation, RAG, fine-tuning, cach... |
| **[promptfoo](https://github.com/promptfoo/promptfoo)**<br/>⭐ 2,100 • TypeScript | 🔧 | 🎯 | prompt engineering, quality assurance, provider comparison | Testing and evaluation framework for LLM prompts with comprehensive CI/CD integration, supporting multiple providers ... |
| **[Multimodal RAG in LlamaCloud](https://www.llamaindex.ai/blog/multimodal-rag-in-llamacloud)** | 🔧 | ⚙️ | document processing, visual QA, enterprise search | Comprehensive guide to implementing Retrieval-Augmented Generation systems that work with both text and image modalit... |

</details>
<details open>
<summary><strong>🛠️ Tools & Utilities</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[ZenML: LLMOps in Production - 287+ Case Studies](https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works)** | 🛡️ | 🎯 | architecture planning, technology selection, team strategy | Comprehensive analysis of 287+ real-world LLMOps implementations, covering successful patterns, common pitfalls, and ... |
| **[MCP for Beginners](https://github.com/microsoft/mcp-for-beginners/)**<br/>⭐ 450 • Multiple | 🔧 | ⚙️ | agent development, tool integration, IDE plugins | Beginner-friendly tutorial and examples for Microsoft's Model Context Protocol (MCP), showing how to build tool-using... |

</details>

---

### 🧠 ML Engineering

*Machine learning frameworks, training tools, and platforms for building and deploying ML systems at scale.*

<details open>
<summary><strong>🛠️ Tools & Utilities</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[ML Practical Use Cases](https://github.com/mallahyari/ml-practical-usecases)**<br/>⭐ 890 • Python | 🛡️ | 🎯 | learning, project templates, proof of concepts | Collection of end-to-end machine learning use cases with practical implementations, covering common business scenario... |

</details>
<details open>
<summary><strong>🧠 ML Frameworks & Training</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[MLX - Apple Machine Learning Framework](https://github.com/ml-explore/mlx)**<br/>⭐ 3,200 • Python | 🔧 | ⚙️ | model training, research, prototyping | High-performance machine learning framework specifically optimized for Apple Silicon, designed for research and exper... |

</details>

---

### 🔧 DevOps & SRE

*Infrastructure automation, monitoring, testing, and reliability engineering tools for production systems.*

<details open>
<summary><strong>🏗️ Infrastructure & DevOps</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome Self-hosted](https://github.com/awesome-selfhosted/awesome-selfhosted)**<br/>⭐ 196,000 • Various | 🛡️ | ⚙️ | lab setups, privacy solutions, cost optimization | Comprehensive catalog of self-hostable network services and web applications, covering alternatives to popular SaaS p... |
| **[Diagrams](https://github.com/mingrammer/diagrams)**<br/>⭐ 23,000 • Python | 🛡️ | 🎯 | architecture documentation, system design, technical presentations | Create cloud system architecture diagrams programmatically using Python code, with support for major cloud providers ... |

</details>
<details open>
<summary><strong>📈 Testing & Performance</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Locust](https://github.com/locustio/locust)**<br/>⭐ 26,800 • Python | 🛡️ | ⚙️ | load testing, performance validation, stress testing | Open-source load testing tool that lets you define test scenarios in plain Python code, supporting distributed testin... |

</details>

---

### 📊 Data Engineering

*Tools for data pipelines, processing, storage, and analytics infrastructure.*

<details open>
<summary><strong>🗄️ SQL & Database Tools</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[SLM SQL](https://github.com/CycloneBoy/slm_sql)**<br/>⭐ 124 • Python | 🧪 | ⚙️ | natural language querying, SQL learning tools, database interfaces | Small Language Model specifically designed for SQL generation and database querying tasks, optimized for natural lang... |

</details>

---

### 🔒 Security

*Security scanning, authentication, compliance, and vulnerability management tools.*

<details open>
<summary><strong>🔒 Security & Compliance</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Trivy](https://github.com/aquasecurity/trivy)**<br/>⭐ 29,000 • Go | 🛡️ | 🎯 | vulnerability scanning, container security, supply chain security | Comprehensive security scanner for containers, filesystems, Git repositories, and Kubernetes that detects vulnerabili... |
| **[kubesec](https://github.com/controlplaneio/kubesec)**<br/>⭐ 1,200 • Go | 🛡️ | 🎯 | security scanning, admission control, CI/CD integration | Security risk analysis tool for Kubernetes resources that scans YAML configurations for potential vulnerabilities and... |

</details>

---

## Quick Wins

*High-impact resources you can implement in under 2 hours - perfect for immediate productivity gains.*

| Resource | Setup Time | Impact | Use Case |
|----------|:----------:|:------:|----------|
| [**Trivy**](https://github.com/aquasecurity/trivy) | 15 min | High | vulnerability scanning, container security |
| [**Diagrams**](https://github.com/mingrammer/diagrams) | 15 min | High | architecture documentation, system design |
| [**kubesec**](https://github.com/controlplaneio/kubesec) | 30 min | High | security scanning, admission control |
| [**ML Practical Use Cases**](https://github.com/mallahyari/ml-practical-usecases) | 30 min | High | learning, project templates |


## Contributing

Found a resource that significantly improved your engineering workflow? 

**Quick Add:** Create an issue with the URL and a brief "why it's useful" note.

**Detailed Add:** Follow the [contribution template](.github/ISSUE_TEMPLATE/add-resource.md).

**Quality Standards:**
- Must have used it successfully in a real project
- Should solve a concrete engineering problem
- Include honest assessment of effort/complexity

---

## Tag Cloud

`architecture` `patterns` `evaluation` `testing` `rag` `performance` `infrastructure` `security` `prompts` `ci-cd` `regression` `case-studies`

---

## Recognition

This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning.

**No affiliate links • No sponsored content • Just honest recommendations**

---

## License

Content and curation by [@taghikhah](https://github.com/taghikhah). Resource descriptions under CC BY 4.0. Code examples under MIT.

⭐ **Star this repo** if you find it valuable • **[Share feedback](../../discussions)**

<!-- Auto-generated from data/resources.yaml on 2025-09-22 14:46:59 -->
