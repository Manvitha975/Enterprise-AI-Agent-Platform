from fastapi import APIRouter, HTTPException

from models.schemas import (
    ResearchRequest,
    ResearchResponse
)

from agents.planner import planner_agent

# Initialize API Router
router = APIRouter()


# ==========================
# Home
# ==========================
@router.get(
    "/",
    tags=["System"],
    summary="Home Endpoint"
)
def home():
    return {
        "project": "Enterprise AI Agent Platform",
        "developer": "Manvitha Ankam",
        "version": "1.0.0",
        "status": "Running Successfully 🚀"
    }


# ==========================
# About
# ==========================
@router.get(
    "/about",
    tags=["System"],
    summary="About the developer"
)
def about():
    return {
        "developer": "Manvitha Ankam"
    }


# ==========================
# Status
# ==========================
@router.get(
    "/status",
    tags=["System"],
    summary="Check API status"
)
def status():
    return {
        "status": "Running"
    }


# ==========================
# AI Agents
# ==========================
@router.get(
    "/agents",
    tags=["AI Agents"],
    summary="Available AI Agents"
)
def agents():
    return {
        "agents": [
            "Planner",
            "Research",
            "Document",
            "Reporter"
        ]
    }


# ==========================
# Contact
# ==========================
@router.get(
    "/contact",
    tags=["Portfolio"],
    summary="Developer Contact"
)
def contact():
    return {
        "email": "ae22b107@smail.iitm.ac.in"
    }


# ==========================
# GitHub
# ==========================
@router.get(
    "/github",
    tags=["Portfolio"],
    summary="Developer GitHub Profile"
)
def github():
    return {
        "github": "https://github.com/Manvitha975"
    }


# ==========================
# LinkedIn
# ==========================
@router.get(
    "/linkedin",
    tags=["Portfolio"],
    summary="Developer LinkedIn Profile"
)
def linkedin():
    return {
        "linkedin": "https://www.linkedin.com/in/manvitha-ankam-250897375"
    }


# ==========================
# Resume
# ==========================
@router.get(
    "/resume",
    tags=["Portfolio"],
    summary="Developer Resume"
)
def resume():
    return {
        "resume": "https://drive.google.com/drive/folders/1ok8xt89xEyU4J3dZfF1qSpxDEYaLxWNA",
        "college": "IIT Madras",
        "degree": "Dual Degree in Aerospace Engineering"
    }


# ==========================
# Skills
# ==========================
@router.get(
    "/skills",
    tags=["Portfolio"],
    summary="Developer Skills"
)
def skills():
    return {
        "skills": [
            "Python",
            "FastAPI",
            "Machine Learning",
            "Deep Learning",
            "Natural Language Processing",
            "Computer Vision"
        ]
    }


# ==========================
# Research Agent API
# ==========================
@router.post(
    "/research",
    response_model=ResearchResponse,
    tags=["AI Agents"],
    summary="Research Query Endpoint",
    description="""
Routes the user's request through the Planner Agent.
The Planner Agent selects the appropriate AI agent to process the task.
Currently supported:
- Research Agent
Future:
- Document Agent
- Report Agent
- Code Agent
"""
)
def research(request: ResearchRequest):

    try:

        answer = planner_agent(request.question)

        return ResearchResponse(
            status="success",
            agent="Research Agent",
            question=request.question,
            answer=answer
        )

    except Exception as e:

        print(f"Research Agent Error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Unable to generate response from Research Agent."
        )