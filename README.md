# Engineering Arsenal 🛠️

> A battle-tested collection of tools, resources, and knowledge that actually moved the needle in real engineering projects. Each entry includes practical metadata, honest assessments, and concrete use cases.

<div align="center">

![Resources](https://img.shields.io/badge/Resources-10-blue?style=for-the-badge) ![Domains](https://img.shields.io/badge/Domains-5-green?style=for-the-badge) ![Last Updated](https://img.shields.io/badge/Updated-September%202025-red?style=for-the-badge)

**[🎯 Quick Navigation](#-quick-navigation) • [⚡ Quick Wins](#-quick-wins) • [🔥 Trending](#-trending) • [🤝 Contributing](#-contributing)**

</div>

---

## 🎯 Quick Navigation

<table align="center">
<tr>
<td align="center" width="150">

### 🤖 **AI/ML**
**4 resources**
[Explore →](#llmopsml)

*LLMOps, RAG, Training*

</td>
<td align="center" width="150">

### 🎓 **Learning**
**2 resources**
[Explore →](#mlengineering)

*Guides, Case Studies*

</td>
<td align="center" width="150">

### 🔧 **DevOps**
**3 resources**
[Explore →](#devopssre)

*Infrastructure, Monitoring*

</td>
</tr>
<tr>
<td align="center">

### 📊 **Data**
**1 resources**
[Explore →](#dataengineering)

*Pipelines, Processing*

</td>
</tr>
</table>

---


## 🤖 AI/ML Engineering

### 📦 General Tools

<table>
<tr>
<td width="60%">

**[ZenML: LLMOps in Production - 287+ Case Studies](https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works)**  
N/A License

Comprehensive analysis of 287+ real-world LLMOps implementations, covering successful patterns, common pitfalls, and technology stack choices across various industries.


**💡 Why it's useful:** Provides reality check for architecture decisions, helps benchmark approaches against proven patterns, and saves months of trial-and-error in production deployments.


</td>
<td width="20%" align="center">

**🟢 Battle-tested**  
⚡ **Low Effort**  
🕐 45 min setup

</td>
<td width="20%">

**Perfect for:**
- Architecture Planning
- Technology Selection
- Team Strategy
- Benchmarking

**Tags:** `case-studies` `production` `mlops` `architecture`

</td>
</tr>
</table>

<table>
<tr>
<td width="60%">

**[MCP for Beginners](https://github.com/microsoft/mcp-for-beginners/)**  
⭐ 450 • Multiple • MIT License

Beginner-friendly tutorial and examples for Microsoft's Model Context Protocol (MCP), showing how to build tool-using agents and IDE integrations.


**💡 Why it's useful:** Clarifies how to expose tools and services to LLMs with stable interfaces, provides foundation for building agentic workflows and editor integrations.


</td>
<td width="20%" align="center">

**🟡 Emerging**  
⚖️ **Medium Effort**  
🕐 120 min setup

</td>
<td width="20%">

**Perfect for:**
- Agent Development
- Tool Integration
- Ide Plugins
- Agentic Workflows

**Tags:** `agents` `protocol` `microsoft` `integration`

</td>
</tr>
</table>

### 🎯 LLMOps & RAG Systems

<table>
<tr>
<td width="60%">

**[promptfoo](https://github.com/promptfoo/promptfoo)**  
⭐ 2,100 • TypeScript • MIT License

Testing and evaluation framework for LLM prompts with comprehensive CI/CD integration, supporting multiple providers and evaluation metrics.


**💡 Why it's useful:** Prevents prompt regression in production, enables systematic comparison of providers/models, and provides automated quality gates for LLM applications.


</td>
<td width="20%" align="center">

**🟡 Emerging**  
⚡ **Low Effort**  
🕐 30 min setup

</td>
<td width="20%">

**Perfect for:**
- Prompt Engineering
- Quality Assurance
- Provider Comparison
- Automated Testing

**Tags:** `evaluation` `prompts` `testing` `ci-cd`

</td>
</tr>
</table>

<table>
<tr>
<td width="60%">

**[Multimodal RAG in LlamaCloud](https://www.llamaindex.ai/blog/multimodal-rag-in-llamacloud)**  
N/A License

Comprehensive guide to implementing Retrieval-Augmented Generation systems that work with both text and image modalities using LlamaIndex and LlamaCloud.


**💡 Why it's useful:** Shows practical pathways to add visual understanding to enterprise RAG systems, handles complex document types with embedded diagrams and charts.


</td>
<td width="20%" align="center">

**🟡 Emerging**  
⚖️ **Medium Effort**  
🕐 120 min setup

</td>
<td width="20%">

**Perfect for:**
- Document Processing
- Visual Qa
- Enterprise Search
- Multimodal Chatbots

**Tags:** `rag` `multimodal` `retrieval` `images`

</td>
</tr>
</table>

<details>
<summary>💡 <strong>Domain Insights</strong> - Click for expert tips</summary>

**🎯 Getting Started with LLMOps RAG:**
1. Start with basic prompt testing (use promptfoo)
2. Read the ZenML case studies for architecture patterns
3. Implement evaluation before scaling
4. Focus on cost optimization early

**⚠️ Common Pitfalls:**
- Over-engineering evaluation frameworks too early
- Ignoring cost implications of model choices
- Insufficient context management strategies

</details>

---


## 🧠 ML Engineering

### 📦 General Tools

<table>
<tr>
<td width="60%">

**[ML Practical Use Cases](https://github.com/mallahyari/ml-practical-usecases)**  
⭐ 890 • Python • MIT License

Collection of end-to-end machine learning use cases with practical implementations, covering common business scenarios and technical patterns.


**💡 Why it's useful:** Provides ready-to-adapt templates for real projects, bridges gap between tutorials and production code, includes best practices and common pitfalls.


</td>
<td width="20%" align="center">

**🟢 Battle-tested**  
⚡ **Low Effort**  
🕐 30 min setup

</td>
<td width="20%">

**Perfect for:**
- Learning
- Project Templates
- Proof Of Concepts
- Team Training

**Tags:** `examples` `templates` `notebooks` `learning`

</td>
</tr>
</table>

### 🧠 ML Frameworks & Training

<table>
<tr>
<td width="60%">

**[MLX - Apple Machine Learning Framework](https://github.com/ml-explore/mlx)**  
⭐ 3,200 • Python • MIT License

High-performance machine learning framework specifically optimized for Apple Silicon, designed for research and experimentation with efficient memory usage.


**💡 Why it's useful:** Enables fast local ML experiments on MacBooks without cloud costs, optimized memory usage for large models, and seamless integration with Apple's ecosystem.


</td>
<td width="20%" align="center">

**🟡 Emerging**  
⚖️ **Medium Effort**  
🕐 60 min setup

</td>
<td width="20%">

**Perfect for:**
- Model Training
- Research
- Prototyping
- Local Inference

**Tags:** `training` `apple-silicon` `performance` `research`

</td>
</tr>
</table>

---


## 🔧 DevOps & SRE

### 🏗️ Infrastructure & DevOps

<table>
<tr>
<td width="60%">

**[Awesome Self-hosted](https://github.com/awesome-selfhosted/awesome-selfhosted)**  
⭐ 196,000 • Various • CC0 License

Comprehensive catalog of self-hostable network services and web applications, covering alternatives to popular SaaS products with deployment instructions.


**💡 Why it's useful:** Discovery engine for privacy-respecting alternatives, cost reduction through self-hosting, learning platform for infrastructure management and service deployment.


</td>
<td width="20%" align="center">

**🟢 Battle-tested**  
⚖️ **Medium Effort**  
🕐 60 min setup

</td>
<td width="20%">

**Perfect for:**
- Lab Setups
- Privacy Solutions
- Cost Optimization
- Learning Infrastructure

**Tags:** `catalog` `infrastructure` `self-hosting` `services`

</td>
</tr>
</table>

<table>
<tr>
<td width="60%">

**[Diagrams](https://github.com/mingrammer/diagrams)**  
⭐ 23,000 • Python • MIT License

Create cloud system architecture diagrams programmatically using Python code, with support for major cloud providers and services.


**💡 Why it's useful:** Enables version-controlled, reproducible architecture documentation that stays in sync with code changes, integrates into CI/CD pipelines for automated documentation.


</td>
<td width="20%" align="center">

**🟢 Battle-tested**  
⚡ **Low Effort**  
🕐 15 min setup

</td>
<td width="20%">

**Perfect for:**
- Architecture Documentation
- System Design
- Technical Presentations
- Infrastructure As Code

**Tags:** `documentation` `architecture` `diagrams` `infrastructure`

</td>
</tr>
</table>

### 📈 Performance & Monitoring

<table>
<tr>
<td width="60%">

**[Locust](https://github.com/locustio/locust)**  
⭐ 26,800 • Python • MIT License

Open-source load testing tool that lets you define test scenarios in plain Python code, supporting distributed testing across multiple machines with real-time monitoring.


**💡 Why it's useful:** Enables realistic performance testing with familiar Python syntax, scales to simulate hundreds of thousands of users, and integrates seamlessly into CI/CD pipelines for automated performance validation.


</td>
<td width="20%" align="center">

**🟢 Battle-tested**  
⚖️ **Medium Effort**  
🕐 45 min setup

</td>
<td width="20%">

**Perfect for:**
- Load Testing
- Performance Validation
- Stress Testing
- Api Testing

**Tags:** `load-testing` `performance` `python` `testing`

</td>
</tr>
</table>

<details>
<summary>💡 <strong>Domain Insights</strong> - Click for expert tips</summary>

**🎯 Getting Started with DevOps SRE:**
1. Begin with infrastructure as code (use Diagrams)
2. Implement monitoring before scaling
3. Automate testing early in the pipeline
4. Focus on observability from day one

**⚠️ Common Pitfalls:**
- Manual configuration without version control
- Ignoring load testing until production issues
- Insufficient monitoring and alerting

</details>

---


## 📊 Data Engineering

### 🗄️ Database & SQL Tools

<table>
<tr>
<td width="60%">

**[SLM SQL](https://github.com/CycloneBoy/slm_sql)**  
⭐ 124 • Python • Apache-2.0 License

Small Language Model specifically designed for SQL generation and database querying tasks, optimized for natural language to SQL conversion.


**💡 Why it's useful:** Provides specialized SQL generation capabilities with better performance than general-purpose models for database tasks, lighter weight than large language models.


</td>
<td width="20%" align="center">

**🔴 Experimental**  
⚖️ **Medium Effort**  
🕐 90 min setup

</td>
<td width="20%">

**Perfect for:**
- Natural Language Querying
- Sql Learning Tools
- Database Interfaces
- Automation

**Tags:** `sql` `language-model` `query-generation` `database`

</td>
</tr>
</table>

---

## 🔥 Trending This Month
*Recently added resources gaining traction*

<div align="center">

| 🚀 **New Addition** | ⭐ **Stars** | 🏷️ **Why It's Hot** |
|---------------------|-------------|-------------------|
| **[Awesome Self-hosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** | 196,000 ↗️ | Discovery engine for privacy-respecting alternatives, cost r... |
| **[Locust](https://github.com/locustio/locust)** | 26,800 ↗️ | Enables realistic performance testing with familiar Python s... |
| **[Diagrams](https://github.com/mingrammer/diagrams)** | 23,000 ↗️ | Enables version-controlled, reproducible architecture docume... |

</div>

## ⚡ Quick Wins
*High-impact resources you can implement in under 2 hours*

<table>
<tr>
<th width="30%">🎯 Resource</th>
<th width="15%">⏱️ Setup</th>
<th width="15%">📈 Impact</th>
<th width="40%">✨ Quick Value</th>
</tr>
<tr>
<td><strong><a href="https://github.com/mingrammer/diagrams">Diagrams</a></strong><br/>Create cloud system architecture diagram...</td>
<td>15 min</td>
<td>🔥 High</td>
<td>Enables version-controlled, reproducible architecture docume...</td>
</tr>
<tr>
<td><strong><a href="https://github.com/mallahyari/ml-practical-usecases">ML Practical Use Cases</a></strong><br/>Collection of end-to-end machine learnin...</td>
<td>30 min</td>
<td>🔥 High</td>
<td>Provides ready-to-adapt templates for real projects, bridges...</td>
</tr>
<tr>
<td><strong><a href="https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works">ZenML: LLMOps in Production - 287+ Case Studies</a></strong><br/>Comprehensive analysis of 287+ real-worl...</td>
<td>45 min</td>
<td>🔥 High</td>
<td>Provides reality check for architecture decisions, helps ben...</td>
</tr>
</table>

## 🏷️ Browse by Category

<div align="center">

**🎯 By Use Case**
[Production Ready](README.md#battle-tested) • [Learning Resources](README.md#learning) • [Weekend Projects](README.md#medium-effort) • [Quick Implementations](README.md#low-effort)

**🔧 By Technology**  
[Python Tools](README.md#python) • [TypeScript/JS](README.md#typescript) • [Docker/K8s](README.md#containers) • [Cloud Native](README.md#cloud)

**⚡ By Effort Level**
[Quick Wins (⚡)](README.md#quick-wins) • [Weekend Projects (⚖️)](README.md#weekend) • [Major Initiatives (🔥)](README.md#major)

</div>

---

## 📊 Repository Insights

<div align="center">
<table>
<tr>
<td align="center">

### 📈 **Growth Stats**
- **Total Resources:** {stats['total_resources']}
- **Domains Covered:** {stats['domains_covered']}
- **Avg GitHub Stars:** {stats['avg_stars']:,.1f}k
- **Community Contributors:** 3

</td>
<td align="center">

### 🏆 **Quality Metrics**
- **Battle-tested:** {stats['battle_tested_pct']}%
- **Production Ready:** {stats['production_ready_pct']}%  
- **Quick Setup (<2hrs):** {stats['quick_setup_pct']}%
- **Regular Updates:** 100%

</td>
</tr>
</table>
</div>

### 🏷️ Popular Tags
{' '.join([f'`{tag}`' for tag, _ in stats['popular_tags']])}

---

## 🤝 Contributing

<div align="center">

Found a resource that significantly improved your engineering workflow?

**[📝 Quick Add via Issue](../../issues/new/choose)** • **[🛠️ Detailed Contribution Guide](CONTRIBUTING.md)** • **[🤖 Use Claude Code Agent](#claude-code-integration)**

</div>

### ✅ Quality Standards
- ✅ **Battle-tested** in real projects
- ✅ **Solves concrete** engineering problems  
- ✅ **Honest assessment** of effort/complexity
- ✅ **Clear practical value** with specific benefits

---

## 🎖️ Recognition

<div align="center">

*This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning.*

**No affiliate links • No sponsored content • Just honest recommendations**

---

**Built with ❤️ by [@yourusername](https://github.com/yourusername)**  
*Licensed under MIT • Content under CC BY 4.0*

⭐ **Star this repo** if you find it valuable • **[Share feedback](../../discussions)**

</div>

<!-- Auto-generated from data/resources.yaml on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -->
