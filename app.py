from fastapi import FastAPI
from routes.api import router

app = FastAPI(
    title="Enterprise AI Agent Platform",
    description="""
An AI-powered multi-agent platform built using FastAPI and Google Gemini.

Features:
- AI Research Agent
- Modular Architecture
- Prompt Engineering
- REST API
""",
    version="1.0.0"
)

app.include_router(router)