from services.search_service import search_web
from services.gemini_service import ask_gemini


def web_search_agent(question: str) -> str:
    """
    Web Search Agent

    Searches the web,
    then asks Gemini
    to summarize the results.
    """

    results = search_web(question)

    prompt = f"""
You are an expert AI assistant.

Below are the web search results.

{results}

Using ONLY the information above,

Provide

1. A concise summary
2. Important points
3. Sources mentioned
4. Final conclusion
"""

    return ask_gemini(prompt)