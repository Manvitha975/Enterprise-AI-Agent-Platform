from services.gemini_service import ask_gemini


def research_agent(question: str) -> str:
    """
    Research Agent

    Responsible for:
    - Understanding the user's question
    - Preparing a professional prompt
    - Calling Gemini
    - Returning the AI response
    """

    prompt = f"""
You are an expert AI Research Assistant.

Your job is to provide accurate, professional, and easy-to-understand explanations.

Follow these rules:

1. Answer in simple English.
2. Use headings.
3. Explain step-by-step.
4. Give at least one real-world example.
5. Keep the response between 250–350 words.
6. If appropriate, include a short summary at the end.
7. If the question is technical, explain important terms before using them.
8. Never make up facts. If you are unsure, clearly mention it.

User Question:
{question}
"""

    return ask_gemini(prompt)