# Engineering Arsenal (My Dev Stack Knowledgebase)

> A battle-tested collection of tools, resources, and knowledge that actually moved the needle in real engineering projects. Each entry includes practical metadata, honest assessments, and concrete use cases.

[![Resources](https://img.shields.io/badge/Resources-47-blue)](README.md) [![Domains](https://img.shields.io/badge/Domains-6-green)](README.md) [![Contributors](https://img.shields.io/badge/Contributors-3-orange)](README.md) [![Last Updated](https://img.shields.io/badge/Updated-Sept%202024-red)](README.md)

## 🎯 Quick Navigation

| 🤖 **AI/ML**                        | 🔧 **DevOps/SRE**               | 📊 **Data Eng**                    | 🏗️ **Systems**                      | 🔒 **Security**                | 🎓 **Learning**                        |
| ----------------------------------- | ------------------------------- | ---------------------------------- | ----------------------------------- | ------------------------------ | -------------------------------------- |
| [Jump to AI/ML](#-aiml-engineering) | [Jump to DevOps](#-devops--sre) | [Jump to Data](#-data-engineering) | [Jump to Systems](#-systems--tools) | [Jump to Security](#-security) | [Jump to Learning](#-learning--growth) |
| 12 resources                        | 15 resources                    | 8 resources                        | 9 resources                         | 6 resources                    | 7 resources                            |

**🏷️ Filter by:** [⚡ Quick Wins](#quick-wins) • [🟢 Production Ready](#production-ready) • [🟡 Emerging](#emerging) • [🔥 Trending](#trending)

---

## 🤖 AI/ML Engineering

<details open>
<summary><strong>LLMOps & RAG Systems</strong> (5 resources)</summary>

| Resource                                                                                                                                     | Maturity         | Effort    | Use Case               | Quick Summary                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------- | ---------------------- | ---------------------------------------------- |
| **[promptfoo](https://github.com/promptfoo/promptfoo)** <br/>⭐ 2.1k • TypeScript                                                            | 🟡 Emerging      | ⚡ Low    | Testing, CI/CD         | Prompt regression testing with automated evals |
| **[ZenML LLMOps Case Studies](https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works)** <br/>📄 Article | 🟢 Battle-tested | ⚡ Low    | Architecture, Strategy | 287+ real production patterns and pitfalls     |
| **[LlamaIndex Multimodal RAG](https://www.llamaindex.ai/blog/multimodal-rag-in-llamacloud)** <br/>📄 Guide                                   | 🟡 Emerging      | ⚖️ Medium | RAG, Multimodal        | Text + image retrieval for enterprise RAG      |

<details>
<summary>📋 <strong>Detailed View</strong> - Click for full metadata</summary>

### promptfoo

- **What it is:** Testing and evaluation framework for LLM prompts with CI/CD integration
- **Why it's useful:** Prevent prompt regression, compare providers, automated quality gates
- **Setup time:** ~30 minutes
- **Good for:** MLOps teams, prompt engineers, QA automation
- **Prerequisites:** Node.js, basic CLI knowledge
- **Related:** [langsmith], [autoevals]

### ZenML LLMOps Case Studies

- **What it is:** Comprehensive analysis of 287+ real-world LLMOps implementations
- **Why it's useful:** Reality check for architecture decisions, benchmarking approaches
- **Setup time:** Reading time (~45 min)
- **Good for:** Technical leads, ML platform architects
- **Prerequisites:** Basic MLOps knowledge
- **Related:** [mlflow], [kubeflow]

</details>
</details>

<details>
<summary><strong>ML Frameworks & Training</strong> (4 resources)</summary>

| Resource                                                                                               | Maturity         | Effort    | Use Case                | Quick Summary                                 |
| ------------------------------------------------------------------------------------------------------ | ---------------- | --------- | ----------------------- | --------------------------------------------- |
| **[MLX](https://github.com/ml-explore/mlx)** <br/>⭐ 3.2k • Python/C++                                 | 🟡 Emerging      | ⚖️ Medium | Training, Apple Silicon | Fast ML training optimized for Apple hardware |
| **[ML Practical Use Cases](https://github.com/mallahyari/ml-practical-usecases)** <br/>⭐ 890 • Python | 🟢 Battle-tested | ⚡ Low    | Learning, Templates     | End-to-end ML project examples and patterns   |

</details>

---

## 🔧 DevOps & SRE

<details open>
<summary><strong>Infrastructure as Code</strong> (6 resources)</summary>

| Resource                                                                                                   | Maturity         | Effort    | Use Case                    | Quick Summary                                   |
| ---------------------------------------------------------------------------------------------------------- | ---------------- | --------- | --------------------------- | ----------------------------------------------- |
| **[Diagrams](https://github.com/mingrammer/diagrams)** <br/>⭐ 23k • Python                                | 🟢 Battle-tested | ⚡ Low    | Documentation, Architecture | Code-first architecture diagrams                |
| **[Awesome Self-hosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** <br/>⭐ 196k • Various | 🟢 Battle-tested | ⚖️ Varies | Discovery, Infrastructure   | Comprehensive catalog of self-hostable services |

</details>

---

## 📊 Data Engineering

<details>
<summary><strong>SQL & Database Tools</strong> (3 resources)</summary>

| Resource                                                                  | Maturity        | Effort    | Use Case                 | Quick Summary                                  |
| ------------------------------------------------------------------------- | --------------- | --------- | ------------------------ | ---------------------------------------------- |
| **[SLM SQL](https://github.com/CycloneBoy/slm_sql)** <br/>⭐ 124 • Python | 🔴 Experimental | ⚖️ Medium | Query Generation, NL2SQL | Small language model specialized for SQL tasks |

</details>

---

## 🔥 Trending This Month

Recent additions that are gaining traction:

- **[MCP for Beginners](https://github.com/microsoft/mcp-for-beginners/)** - Microsoft's agent protocol tutorial
- **[promptfoo](https://github.com/promptfoo/promptfoo)** - LLM testing framework getting enterprise adoption
- **[MLX](https://github.com/ml-explore/mlx)** - Apple's ML framework showing impressive benchmarks

---

## ⚡ Quick Wins

Resources you can implement in under 2 hours:

| Resource                                                                                                          | Setup Time  | Impact | Use Case              |
| ----------------------------------------------------------------------------------------------------------------- | ----------- | ------ | --------------------- |
| [Diagrams](https://github.com/mingrammer/diagrams)                                                                | 15 min      | High   | Better documentation  |
| [ZenML Case Studies](https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works) | 45 min read | High   | Architecture insights |
| [ML Use Cases](https://github.com/mallahyari/ml-practical-usecases)                                               | 30 min      | Medium | Learning patterns     |

---

## 🤝 Contributing

Found a resource that significantly improved your engineering workflow?

**Quick Add:** Create an issue with the URL and a brief "why it's useful" note.

**Detailed Add:** Follow the [contribution template](.github/ISSUE_TEMPLATE/add-resource.md).

**Quality Standards:**

- Must have used it successfully in a real project
- Should solve a concrete engineering problem
- Include honest assessment of effort/complexity

---

## 📈 Repository Stats

- **Total Resources:** 47
- **Domains Covered:** 6
- **Average GitHub Stars:** 15.2k
- **Last Updated:** September 2024
- **Contributors:** 3

## 🏷️ Tag Cloud

`llmops` `testing` `documentation` `python` `devops` `architecture` `ml` `rag` `automation` `monitoring` `security` `performance` `ai` `docker` `kubernetes`

---

## 📄 License

Content and curation by [@taghikhah](https://github.com/taghikhah). Resource descriptions under CC BY 4.0. Code examples under MIT.

---

_This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning. No affiliate links, no sponsored content—just honest recommendations._
