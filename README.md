# 🤖 Enterprise AI Agent Platform# 🤖 AgentOS

An Enterprise Multi-Agent AI Operating System

Built using FastAPI, LangGraph, Gemini, RAG, Docker and AWS.

> A production-ready multi-agent AI platform that automates research, document intelligence, code generation, and report creation using collaborative AI agents.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-yellow)

---

# 📖 Overview

Enterprise AI Agent Platform is an intelligent multi-agent system designed to automate complex workflows by combining Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector search, and workflow orchestration.

Instead of relying on a single chatbot, the platform coordinates specialized AI agents that collaborate to perform research, analyze documents, generate code, and produce structured reports.

The project demonstrates modern AI application development using production-grade software engineering practices.

---

# 🚀 Key Features

- 🤖 Multi-Agent Workflow
- 📄 Document Intelligence (PDF, DOCX, TXT)
- 🔍 Retrieval-Augmented Generation (RAG)
- 🧠 AI Research Assistant
- 💻 AI Code Generation
- 📝 Automated Report Generation
- 💬 Conversational Chat Interface
- 📊 Real-Time Workflow Dashboard
- 🐳 Dockerized Deployment
- ☁️ Cloud Deployment on AWS EC2

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
               FastAPI Backend
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Planner Agent   Research Agent   Document Agent
      │               │               │
      └───────────────┼───────────────┘
                      ▼
                Report Agent
                      │
                      ▼
               Final AI Response
```

---

# 🧩 AI Agents

## 🧠 Planner Agent

- Breaks complex tasks into smaller subtasks
- Coordinates execution between agents

---

## 🔍 Research Agent

- Searches the web
- Summarizes information
- Collects references

---

## 📄 Document Agent

- Reads uploaded PDFs
- Performs semantic search
- Answers questions using RAG

---

## 💻 Coding Agent

- Generates code
- Debugs Python programs
- Explains algorithms

---

## 📝 Report Agent

- Combines outputs from all agents
- Produces structured reports
- Generates Markdown and PDF summaries

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- Python

## AI

- Google Gemini API
- LangChain
- LangGraph

## Vector Database

- Qdrant

## Database

- PostgreSQL

## Frontend

- Streamlit

## Deployment

- Docker
- AWS EC2

---

# 📂 Project Structure

```
Enterprise-AI-Agent-Platform/

│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── document.py
│   ├── coder.py
│   └── reporter.py
│
├── rag/
│   ├── ingest.py
│   ├── embeddings.py
│   └── retriever.py
│
├── database/
│   └── postgres.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│
├── tests/
│
└── docker/
```

---

# 📅 Development Roadmap

## ✅ Phase 1

- [ ] GitHub Repository
- [ ] FastAPI Backend
- [ ] API Routing
- [ ] Pydantic Models

---

## 🚧 Phase 2

- [ ] Gemini API Integration
- [ ] Research Agent
- [ ] Chat API

---

## 🚧 Phase 3

- [ ] PDF Upload
- [ ] Embeddings
- [ ] Qdrant Integration
- [ ] RAG Pipeline

---

## 🚧 Phase 4

- [ ] Multi-Agent Workflow using LangGraph
- [ ] Planner Agent
- [ ] Reporter Agent

---

## 🚧 Phase 5

- [ ] Docker
- [ ] PostgreSQL
- [ ] AWS EC2 Deployment

---

# 🎯 Learning Objectives

This project is designed to gain hands-on experience with:

- FastAPI
- Backend Development
- REST APIs
- Pydantic
- LLM Integration
- Prompt Engineering
- Retrieval-Augmented Generation
- Vector Databases
- Multi-Agent Systems
- LangGraph
- Docker
- PostgreSQL
- AWS Cloud Deployment
- Production AI System Design

---

# 📌 Future Improvements

- User Authentication
- Multi-user Support
- Agent Memory
- Voice Assistant
- Calendar Integration
- Slack & Teams Integration
- Email Automation
- Knowledge Graph Support
- Monitoring Dashboard

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

# 👩‍💻 Author

**Manvitha Ankam**

Dual Degree (B.Tech + M.Tech)  in Aerospace Engineering 
Indian Institute of Technology Madras

GitHub: https://github.com/Manvitha975

LinkedIn: https://www.linkedin.com/in/manvitha-ankam-250897375/

---

⭐ If you find this project useful, consider giving it a star.
