from agents.researcher import research_agent
from agents.web_search import web_search_agent


from services.gemini_service import ask_gemini


def planner_agent(question: str) -> str:
    """
    Planner Agent

    Uses Gemini to decide
    which specialized AI Agent
    should execute the request.
    """

    routing_prompt = f"""
You are the Planner Agent of an AI system.

Choose ONLY ONE agent.

Available Agents:

1. Research
Use for:
- Definitions
- Explanations
- Comparisons
- Concepts
- General knowledge

2. Search
Use for:
- Latest news
- Current events
- Today's information
- Recent updates

3. Document
Use for:
- PDF
- Files
- Documents
- Summaries
- Reports

Return ONLY ONE WORD.

Research

OR

Search

OR

Document

User Request:

{question}
"""

    decision = ask_gemini(routing_prompt).strip()

    print(f"\nPlanner Decision: {decision}\n")

    if "Search" in decision:
        return web_search_agent(question)

    elif "Document" in decision:
        return (
            "Please upload your PDF using "
            "POST /document/summarize."
        )

    else:
        return research_agent(question)