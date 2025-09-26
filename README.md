# Engineering Arsenal (Knowledgebase)

A curated, enterprise-grade collection of links, repos, and notes that actually helped me build real systems (AI, Platform, Data, Security, Developer Tools). Each entry includes structured metadata, honest assessments, and why it's useful in practice.

<div align="center">

![Resources](https://img.shields.io/badge/Resources-52-blue) ![Domains](https://img.shields.io/badge/Domains-5-green) ![Contributors](https://img.shields.io/badge/Contributors-1-orange) ![Last Updated](https://img.shields.io/badge/Updated-September%202025-red)

</div>


### Quick Navigation

<div align="center">

| 🤖 **AI Engineering** | 🏗️ **Platform Engineering** | 🛠️ **Developer Tools** | 📊 **Data Engineering** | 🔒 **Security** |
|:------------:|:------------:|:------------:|:------------:|:------------:|
| [Jump to AI Engineering](#ai-engineering) | [Jump to Platform Engineering](#platform-engineering) | [Jump to Developer Tools](#developer-tools) | [Jump to Data Engineering](#data-engineering) | [Jump to Security](#security) |
| **36 resources** | **13 resources** | **14 resources** | **5 resources** | **3 resources** |
| *Agents, RAG & ML systems* | *Infrastructure & reliability* | *Development utilities* | *Data pipelines & processing* | *Security & compliance* |

</div>

<div align="center">

[![Quick Wins](https://img.shields.io/badge/⚡_Quick_Wins-Under_2hrs-brightgreen)](#quick-wins) &nbsp;&nbsp;[![Production Ready](https://img.shields.io/badge/🛡️_Production_Ready-Battle_tested-blue)](#production-ready) &nbsp;&nbsp;[![Emerging Tools](https://img.shields.io/badge/🔧_Emerging-Worth_watching-orange)](#emerging-tools)

</div>


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


### 🤖 AI Engineering

*Agents/MCP, RAG & knowledge systems, testing & eval, training & frameworks, architecture.*

<details>
<summary><strong>Agent Systems & Integration</strong> (17 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome MCP Servers <small>&#10548;</small>](https://github.com/punkpeye/awesome-mcp-servers)**<br/>⭐ 70.9K | 🛡️ | 🚀 | MCP server discovery, ecosystem exploration, integration planning | Comprehensive curated list of 20+ categories of MCP servers covering aerospace, biology, cloud platforms, coding, and... |
| **[DeepLearning.AI: Build Rich-Context AI Apps with MCP <small>&#10548;</small>](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/)** | 🛡️ | 🎯 | MCP protocol learning, AI application development, standardization strategy | Hands-on course developed with Anthropic teaching MCP protocol for building standardized AI applications with externa... |
| **[LangGraph Agent Architectures Concepts <small>&#10548;</small>](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#agent-architectures)** | 🛡️ | 🎯 | agent system design, workflow automation, intelligent applications | Comprehensive guide to agent architectures where LLMs control application flow, covering routers, tool-calling agents... |
| **[LangGraph Multi-Agent Systems Documentation <small>&#10548;</small>](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)** | 🛡️ | 🎯 | multi-agent system design, agent coordination, complex AI workflows | Comprehensive documentation on multi-agent architectures including network, supervisor, hierarchical patterns with co... |
| **[MCP.so - MCP Server Directory <small>&#10548;</small>](https://mcp.so/)** | 🛡️ | 🎯 | MCP server discovery, integration planning, documentation access | Community-driven platform cataloging 16,624+ MCP servers and clients with categorized listings, installation guides, ... |
| **[Function Calling vs MCP: What You Need to Know <small>&#10548;</small>](https://blog.fotiecodes.com/function-calling-vs-model-context-protocol-mcp-what-you-need-to-know-cm88zfwik000108ji0a1d54fc)** | 🛡️ | 🚀 | AI system architecture, protocol comparison, integration planning | Comprehensive technical comparison of Function Calling and Model Context Protocol (MCP), explaining how function call... |
| **[Graphiti - Real-Time Knowledge Graphs for AI <small>&#10548;</small>](https://github.com/getzep/graphiti)**<br/>⭐ 18.4K | 🔧 | 🎯 | AI agent memory, knowledge graph RAG, temporal data tracking | Framework for building real-time knowledge graphs that dynamically integrate user interactions, structured/unstructur... |
| **[Browser Use <small>&#10548;</small>](https://github.com/browser-use/browser-use)**<br/>⭐ 70.5K | 🔧 | 🚀 | automated web tasks, browser automation, AI-driven web interactions | AI-powered browser automation framework enabling agents to control web browsers, automate online tasks, and interact ... |
| **[CopilotKit <small>&#10548;</small>](https://github.com/CopilotKit/CopilotKit)**<br/>⭐ 23.9K | 🔧 | 🎯 | AI chatbots, in-app assistants, agentic interfaces | React framework for building AI copilots and in-app AI agents with elegant UI components, security features, and rapi... |
| **[Agent Development Kit (ADK) <small>&#10548;</small>](https://github.com/google/adk-python)**<br/>⭐ 13.2K | 🔧 | 🎯 | intelligent assistants, multi-agent workflows, enterprise AI solutions | Open-source Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexible architecture... |
| **[Parlant <small>&#10548;</small>](https://github.com/emcie-co/parlant)**<br/>⭐ 12.5K | 🔧 | 🎯 | compliant AI agents, financial services AI, healthcare chatbots | Python framework for building AI agents with guaranteed rule compliance and predictable behavior through dynamic guid... |
| **[Claude Context - MCP Semantic Code Search <small>&#10548;</small>](https://github.com/zilliztech/claude-context)**<br/>⭐ 3.7K | 🔧 | 🎯 | AI code assistance, semantic code search, context management | MCP plugin enabling semantic code search for AI coding agents like Claude Code, providing efficient codebase indexing... |
| **[MCP for Beginners <small>&#10548;</small>](https://github.com/microsoft/mcp-for-beginners/)**<br/>⭐ <1K | 🔧 | 🚀 | agent development, tool integration, IDE plugins | Beginner-friendly tutorial and examples for Microsoft's Model Context Protocol (MCP), showing how to build tool-using... |
| **[Agent2Agent (A2A) Protocol <small>&#10548;</small>](https://github.com/a2aproject/A2A)**<br/>⭐ 19.9K | 🧪 | 🎯 | cross-platform agent communication, secure agent collaboration, enterprise AI integration | Open protocol enabling secure communication and interoperability between AI agents from different frameworks while pr... |
| **[MCP Chrome Extension <small>&#10548;</small>](https://github.com/hangwin/mcp-chrome)**<br/>⭐ 8.1K | 🧪 | 🚀 | browser automation, web scraping, content analysis | Chrome extension transforming browsers into AI-controlled automation tools with 20+ tools for browser management, con... |
| **[ART - Agent Reinforcement Trainer <small>&#10548;</small>](https://github.com/OpenPipe/ART)**<br/>⭐ 7.4K | 🧪 | 🚀 | agent training, reinforcement learning, AI skill development | Reinforcement learning framework for training multi-step AI agents using GRPO with automatic reward generation and ze... |
| **[Ableton MCP - AI Music Production <small>&#10548;</small>](https://github.com/ahujasid/ableton-mcp)**<br/>⭐ 1.9K | 🧪 | 🚀 | AI music creation, creative automation, experimental music | AI-powered integration allowing Claude to directly control Ableton Live for prompt-assisted music production, track c... |

</details>
<details>
<summary><strong>RAG & Knowledge Systems</strong> (6 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[GraphRAG Official Documentation <small>&#10548;</small>](https://graphrag.com/)** | 🛡️ | 🚀 | GraphRAG learning, implementation planning, reference documentation | Comprehensive documentation hub for GraphRAG covering conceptual overviews, how-to guides, technical references, and ... |
| **[Essential GraphRAG: Knowledge Graph-Enhanced RAG <small>&#10548;</small>](https://neo4j.com/essential-graphrag/)** | 🛡️ | 🎯 | GraphRAG learning, system implementation, LLM accuracy improvement | Free 176-page Manning book by Neo4j experts covering GraphRAG implementation, vector similarity, knowledge graph cons... |
| **[LLM Patterns: A Comprehensive Guide <small>&#10548;</small>](https://eugeneyan.com/writing/llm-patterns/)** | 🛡️ | 🎯 | system architecture, pattern implementation, production design | Comprehensive exploration of practical patterns for building LLM systems, covering evaluation, RAG, fine-tuning, cach... |
| **[Neo4j GraphRAG Field Guide: 9 RAG Patterns <small>&#10548;</small>](https://neo4j.com/developer-blog/graphrag-field-guide-rag-patterns/)** | 🛡️ | 🎯 | GraphRAG implementation, pattern selection, system architecture | Structured guide to 9 GraphRAG patterns across basic, intermediate, and advanced levels including vector search, comm... |
| **[nano-graphrag - Lightweight GraphRAG Implementation <small>&#10548;</small>](https://github.com/gusye1234/nano-graphrag)**<br/>⭐ 3.4K | 🔧 | 🚀 | GraphRAG learning, rapid prototyping, custom implementations | Simplified, hackable GraphRAG implementation in ~1,100 lines with flexible components for LLM, embedding, vector stor... |
| **[Multimodal RAG in LlamaCloud <small>&#10548;</small>](https://www.llamaindex.ai/blog/multimodal-rag-in-llamacloud)** | 🔧 | 🚀 | document processing, visual QA, enterprise search | Comprehensive guide to implementing Retrieval-Augmented Generation systems that work with both text and image modalit... |

</details>
<details>
<summary><strong>Testing & Evaluation</strong> (4 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome ChatGPT Prompts <small>&#10548;</small>](https://github.com/f/awesome-chatgpt-prompts)**<br/>⭐ 134K | 🛡️ | 🚀 | prompt engineering, AI interaction design, role-playing scenarios | Curated collection of ChatGPT prompts for various roles and scenarios, providing templates for effective AI interacti... |
| **[Generative AI for Beginners <small>&#10548;</small>](https://github.com/microsoft/generative-ai-for-beginners)**<br/>⭐ 98.8K | 🛡️ | 🚀 | AI education, skill development, team training | Free 21-lesson course teaching everything needed to build generative AI applications, created by Microsoft Cloud Advo... |
| **[Evidently <small>&#10548;</small>](https://github.com/evidentlyai/evidently)**<br/>⭐ 6.6K | 🛡️ | 🎯 | model monitoring, data drift detection, ML evaluation | Open-source Python library for ML and LLM observability with 100+ built-in metrics for evaluating, testing, and monit... |
| **[promptfoo <small>&#10548;</small>](https://github.com/promptfoo/promptfoo)**<br/>⭐ 2.1K | 🔧 | 🎯 | prompt engineering, quality assurance, provider comparison | Testing and evaluation framework for LLM prompts with comprehensive CI/CD integration, supporting multiple providers ... |

</details>
<details>
<summary><strong>Training & Frameworks</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[LLM Course <small>&#10548;</small>](https://github.com/mlabonne/llm-course)**<br/>⭐ 62.7K | 🛡️ | 🚀 | LLM education, self-paced learning, team training | Comprehensive free course for learning Large Language Models with structured roadmap, practical Colab notebooks, and ... |
| **[MLX - Apple Machine Learning Framework <small>&#10548;</small>](https://github.com/ml-explore/mlx)**<br/>⭐ 3.2K | 🔧 | 🚀 | model training, research, prototyping | High-performance machine learning framework specifically optimized for Apple Silicon, designed for research and exper... |

</details>
<details>
<summary><strong>Core AI Tools</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome MLOps <small>&#10548;</small>](https://github.com/visenger/awesome-mlops)**<br/>⭐ 13.3K | 🛡️ | 🚀 | MLOps learning, resource discovery, technology selection | Curated reference list for Machine Learning Operations covering workflow management, feature stores, deployment, moni... |
| **[Firecrawl <small>&#10548;</small>](https://github.com/firecrawl/firecrawl)**<br/>⭐ 59.3K | 🔧 | 🎯 | data extraction, AI training data, web scraping automation | Web data API service that crawls entire websites and converts content into LLM-ready markdown or structured data with... |

</details>
<details>
<summary><strong>Architecture & Best Practices</strong> (4 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[How to Match LLM Patterns to Problems <small>&#10548;</small>](https://eugeneyan.com/writing/llm-problems/)** | 🛡️ | 🎯 | problem diagnosis, solution selection, performance optimization | Systematic framework for identifying and solving common LLM implementation challenges, covering performance, reliabil... |
| **[ML System Design: 650+ Case Studies Database <small>&#10548;</small>](https://www.evidentlyai.com/ml-system-design)** | 🛡️ | 🚀 | system architecture, design decisions, industry benchmarking | Curated database of 650+ ML and LLM case studies from 100+ companies including Netflix, Airbnb, and DoorDash, coverin... |
| **[ZenML: LLMOps in Production - 287+ Case Studies <small>&#10548;</small>](https://www.zenml.io/blog/llmops-in-production-287-more-case-studies-of-what-actually-works)** | 🛡️ | 🚀 | architecture planning, technology selection, team strategy | Comprehensive analysis of 287+ real-world LLMOps implementations, covering successful patterns, common pitfalls, and ... |
| **[ML Practical Use Cases <small>&#10548;</small>](https://github.com/mallahyari/ml-practical-usecases)**<br/>⭐ <1K | 🛡️ | 🚀 | learning, project templates, proof of concepts | Collection of end-to-end machine learning use cases with practical implementations, covering common business scenario... |

</details>
<details>
<summary><strong>Small Language Models & Specialized AI</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Granite Docling 258M <small>&#10548;</small>](https://huggingface.co/ibm-granite/granite-docling-258M)** | 🔧 | 🎯 | document conversion for RAG, PDF to markdown processing, structured data extraction | Ultra-compact 258M parameter vision-language model specialized for document conversion and understanding, capable of ... |

</details>

---

### 🏗️ Platform Engineering

*Observability & performance, infra & services (IaC), container platforms, build & delivery, docs/runbooks.*

<details>
<summary><strong>Infrastructure & Services</strong> (4 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome Self-hosted <small>&#10548;</small>](https://github.com/awesome-selfhosted/awesome-selfhosted)**<br/>⭐ 196K | 🛡️ | 🚀 | lab setups, privacy solutions, cost optimization | Comprehensive catalog of self-hostable network services and web applications, covering alternatives to popular SaaS p... |
| **[LiveKit <small>&#10548;</small>](https://github.com/livekit/livekit)**<br/>⭐ 14.9K | 🛡️ | 🎯 | video conferencing, live streaming, real-time collaboration | Open-source real-time communication platform providing scalable WebRTC infrastructure for building video, audio, and ... |
| **[Awesome MLOps <small>&#10548;</small>](https://github.com/visenger/awesome-mlops)**<br/>⭐ 13.3K | 🛡️ | 🚀 | MLOps learning, resource discovery, technology selection | Curated reference list for Machine Learning Operations covering workflow management, feature stores, deployment, moni... |
| **[Diagrams <small>&#10548;</small>](https://github.com/mingrammer/diagrams)**<br/>⭐ 23K | 🛡️ | 🚀 | architecture documentation, system design, technical presentations | Create cloud system architecture diagrams programmatically using Python code, with support for major cloud providers ... |

</details>
<details>
<summary><strong>Platform Tools</strong> (4 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[SurrealDB <small>&#10548;</small>](https://github.com/surrealdb/surrealdb)**<br/>⭐ 30.1K | 🛡️ | 🎯 | real-time applications, modern web development, complex data relationships | Multi-model database combining document, graph, and relational data models with built-in API layer, real-time subscri... |
| **[Task <small>&#10548;</small>](https://github.com/go-task/task)**<br/>⭐ 13.8K | 🛡️ | 🎯 | build automation, task orchestration, workflow management | Simple task runner and build tool written in Go, designed as a modern alternative to GNU Make with YAML-based configu... |
| **[kubesec <small>&#10548;</small>](https://github.com/controlplaneio/kubesec)**<br/>⭐ 1.2K | 🛡️ | 🎯 | security scanning, admission control, CI/CD integration | Security risk analysis tool for Kubernetes resources that scans YAML configurations for potential vulnerabilities and... |
| **[Agent2Agent (A2A) Protocol <small>&#10548;</small>](https://github.com/a2aproject/A2A)**<br/>⭐ 19.9K | 🧪 | 🎯 | cross-platform agent communication, secure agent collaboration, enterprise AI integration | Open protocol enabling secure communication and interoperability between AI agents from different frameworks while pr... |

</details>
<details>
<summary><strong>Container Platforms</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Trivy <small>&#10548;</small>](https://github.com/aquasecurity/trivy)**<br/>⭐ 29K | 🛡️ | 🎯 | vulnerability scanning, container security, supply chain security | Comprehensive security scanner for containers, filesystems, Git repositories, and Kubernetes that detects vulnerabili... |

</details>
<details>
<summary><strong>Performance & Observability</strong> (3 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[k6 <small>&#10548;</small>](https://github.com/grafana/k6)**<br/>⭐ 28.8K | 🛡️ | 🎯 | load testing, performance validation, CI/CD integration | Modern load testing tool using Go and JavaScript for performance testing with developer-friendly scripting and extens... |
| **[Locust <small>&#10548;</small>](https://github.com/locustio/locust)**<br/>⭐ 26.8K | 🛡️ | 🎯 | load testing, performance validation, stress testing | Open-source load testing tool that lets you define test scenarios in plain Python code, supporting distributed testin... |
| **[Dozzle <small>&#10548;</small>](https://github.com/amir20/dozzle)**<br/>⭐ 9.6K | 🔧 | 🚀 | container debugging, log monitoring, development workflow | Lightweight real-time log viewer for Docker containers with intelligent search, split-screen viewing, and multi-conta... |

</details>
<details>
<summary><strong>Documentation & Architecture</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome System Design Resources <small>&#10548;</small>](https://github.com/ashishps1/awesome-system-design-resources)**<br/>⭐ 26.1K | 🛡️ | 🚀 | interview preparation, system design learning, architecture planning | Comprehensive curated list of free system design learning resources including concepts, patterns, interview problems,... |

</details>

---

### 🛠️ Developer Tools

*Code quality, browser/web tools, CLI/editors/productivity, creative/specialized.*

<details>
<summary><strong>Development Utilities</strong> (9 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome MCP Servers <small>&#10548;</small>](https://github.com/punkpeye/awesome-mcp-servers)**<br/>⭐ 70.9K | 🛡️ | 🚀 | MCP server discovery, ecosystem exploration, integration planning | Comprehensive curated list of 20+ categories of MCP servers covering aerospace, biology, cloud platforms, coding, and... |
| **[MCP.so - MCP Server Directory <small>&#10548;</small>](https://mcp.so/)** | 🛡️ | 🎯 | MCP server discovery, integration planning, documentation access | Community-driven platform cataloging 16,624+ MCP servers and clients with categorized listings, installation guides, ... |
| **[Awesome Self-hosted <small>&#10548;</small>](https://github.com/awesome-selfhosted/awesome-selfhosted)**<br/>⭐ 196K | 🛡️ | 🚀 | lab setups, privacy solutions, cost optimization | Comprehensive catalog of self-hostable network services and web applications, covering alternatives to popular SaaS p... |
| **[Locust <small>&#10548;</small>](https://github.com/locustio/locust)**<br/>⭐ 26.8K | 🛡️ | 🎯 | load testing, performance validation, stress testing | Open-source load testing tool that lets you define test scenarios in plain Python code, supporting distributed testin... |
| **[LiveKit <small>&#10548;</small>](https://github.com/livekit/livekit)**<br/>⭐ 14.9K | 🛡️ | 🎯 | video conferencing, live streaming, real-time collaboration | Open-source real-time communication platform providing scalable WebRTC infrastructure for building video, audio, and ... |
| **[Task <small>&#10548;</small>](https://github.com/go-task/task)**<br/>⭐ 13.8K | 🛡️ | 🎯 | build automation, task orchestration, workflow management | Simple task runner and build tool written in Go, designed as a modern alternative to GNU Make with YAML-based configu... |
| **[Diagrams <small>&#10548;</small>](https://github.com/mingrammer/diagrams)**<br/>⭐ 23K | 🛡️ | 🚀 | architecture documentation, system design, technical presentations | Create cloud system architecture diagrams programmatically using Python code, with support for major cloud providers ... |
| **[MCP for Beginners <small>&#10548;</small>](https://github.com/microsoft/mcp-for-beginners/)**<br/>⭐ <1K | 🔧 | 🚀 | agent development, tool integration, IDE plugins | Beginner-friendly tutorial and examples for Microsoft's Model Context Protocol (MCP), showing how to build tool-using... |
| **[SLM SQL <small>&#10548;</small>](https://github.com/CycloneBoy/slm_sql)**<br/>⭐ <1K | 🧪 | 🚀 | natural language querying, SQL learning tools, database interfaces | Small Language Model specifically designed for SQL generation and database querying tasks, optimized for natural lang... |

</details>
<details>
<summary><strong>Code Quality & Standards</strong> (3 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Prettier <small>&#10548;</small>](https://github.com/prettier/prettier)**<br/>⭐ 51K | 🛡️ | 🎯 | code formatting, style consistency, automated formatting | Opinionated code formatter that automatically reformats code to enforce consistent styling across JavaScript, TypeScr... |
| **[Husky <small>&#10548;</small>](https://github.com/typicode/husky)**<br/>⭐ 34.2K | 🛡️ | 🎯 | git hook automation, pre-commit checks, workflow enforcement | Lightweight native Git hooks manager that automates workflow enforcement with cross-platform support for all client-s... |
| **[lint-staged <small>&#10548;</small>](https://github.com/lint-staged/lint-staged)**<br/>⭐ 14.2K | 🛡️ | 🎯 | pre-commit validation, code quality enforcement, automated formatting | Runs linters and formatters only on git staged files before commits, preventing problematic code from entering the re... |

</details>
<details>
<summary><strong>Browser & Web Tools</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Browser Use <small>&#10548;</small>](https://github.com/browser-use/browser-use)**<br/>⭐ 70.5K | 🔧 | 🚀 | automated web tasks, browser automation, AI-driven web interactions | AI-powered browser automation framework enabling agents to control web browsers, automate online tasks, and interact ... |
| **[MCP Chrome Extension <small>&#10548;</small>](https://github.com/hangwin/mcp-chrome)**<br/>⭐ 8.1K | 🧪 | 🚀 | browser automation, web scraping, content analysis | Chrome extension transforming browsers into AI-controlled automation tools with 20+ tools for browser management, con... |

</details>

---

### 📊 Data Engineering

*Discovery & governance, query & storage, pipelines & orchestration, analytics & BI.*

<details>
<summary><strong>Data Discovery & Catalogs</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Awesome Public Datasets <small>&#10548;</small>](https://github.com/awesomedata/awesome-public-datasets)**<br/>⭐ 67.8K | 🛡️ | 🚀 | dataset discovery, research projects, machine learning training | Curated collection of high-quality public datasets across 30+ domains including agriculture, biology, climate, financ... |

</details>
<details>
<summary><strong>Query & Database Tools</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[SurrealDB <small>&#10548;</small>](https://github.com/surrealdb/surrealdb)**<br/>⭐ 30.1K | 🛡️ | 🎯 | real-time applications, modern web development, complex data relationships | Multi-model database combining document, graph, and relational data models with built-in API layer, real-time subscri... |
| **[SLM SQL <small>&#10548;</small>](https://github.com/CycloneBoy/slm_sql)**<br/>⭐ <1K | 🧪 | 🚀 | natural language querying, SQL learning tools, database interfaces | Small Language Model specifically designed for SQL generation and database querying tasks, optimized for natural lang... |

</details>
<details>
<summary><strong>Data Infrastructure</strong> (2 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Evidently <small>&#10548;</small>](https://github.com/evidentlyai/evidently)**<br/>⭐ 6.6K | 🛡️ | 🎯 | model monitoring, data drift detection, ML evaluation | Open-source Python library for ML and LLM observability with 100+ built-in metrics for evaluating, testing, and monit... |
| **[Firecrawl <small>&#10548;</small>](https://github.com/firecrawl/firecrawl)**<br/>⭐ 59.3K | 🔧 | 🎯 | data extraction, AI training data, web scraping automation | Web data API service that crawls entire websites and converts content into LLM-ready markdown or structured data with... |

</details>

---

### 🔒 Security

*Supply chain & vuln mgmt, infra/runtime security, secrets/auth/compliance.*

<details>
<summary><strong>Vulnerability Management</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Trivy <small>&#10548;</small>](https://github.com/aquasecurity/trivy)**<br/>⭐ 29K | 🛡️ | 🎯 | vulnerability scanning, container security, supply chain security | Comprehensive security scanner for containers, filesystems, Git repositories, and Kubernetes that detects vulnerabili... |

</details>
<details>
<summary><strong>Infrastructure Security</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[kubesec <small>&#10548;</small>](https://github.com/controlplaneio/kubesec)**<br/>⭐ 1.2K | 🛡️ | 🎯 | security scanning, admission control, CI/CD integration | Security risk analysis tool for Kubernetes resources that scans YAML configurations for potential vulnerabilities and... |

</details>
<details>
<summary><strong>Access & Compliance</strong> (1 resources)</summary>

| Resource | Maturity | Effort | Use Case | Quick Summary |
|----------|:--------:|:------:|----------|---------------|
| **[Parlant <small>&#10548;</small>](https://github.com/emcie-co/parlant)**<br/>⭐ 12.5K | 🔧 | 🎯 | compliant AI agents, financial services AI, healthcare chatbots | Python framework for building AI agents with guaranteed rule compliance and predictable behavior through dynamic guid... |

</details>

---

## Quick Wins

*Best quick win in each domain - high-impact resources you can implement quickly.*

| Domain | Use Case | Resource |
|:------|----------|----------|
| AI-Engineering | model monitoring, data drift detection | **[Evidently <small>&#10548;</small>](https://github.com/evidentlyai/evidently)** |
| Data-Engineering | real-time applications, modern web development | **[SurrealDB <small>&#10548;</small>](https://github.com/surrealdb/surrealdb)** |
| Developer-Tools | code formatting, style consistency | **[Prettier <small>&#10548;</small>](https://github.com/prettier/prettier)** |
| Platform-Engineering | load testing, performance validation | **[k6 <small>&#10548;</small>](https://github.com/grafana/k6)** |
| Security | vulnerability scanning, container security | **[Trivy <small>&#10548;</small>](https://github.com/aquasecurity/trivy)** |


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

`agents` `architecture` `learning` `automation` `mcp` `patterns` `protocol` `graph-rag` `evaluation` `retrieval` `performance` `catalog`

---

## Recognition

This arsenal reflects real engineering experience. Every resource has been battle-tested in production or significantly advanced learning.

**No affiliate links • No sponsored content • Just honest recommendations**

---

## License

Content and curation by [@taghikhah](https://github.com/taghikhah). Resource descriptions under CC BY 4.0. Code examples under MIT.

⭐ **Star this repo** if you find it valuable • **[Share feedback](../../discussions)**

<!-- Auto-generated from data/resources.yaml on 2025-09-26 10:10:46 -->
