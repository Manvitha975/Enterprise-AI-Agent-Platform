from services.pdf_service import extract_text_from_pdf
from services.gemini_service import ask_gemini


def summarize_pdf(pdf_path: str) -> str:
    """
    Summarizes a PDF using Gemini.
    """

    text = extract_text_from_pdf(pdf_path)

    prompt = f"""
You are an expert document analyst.

Read the following document.

Provide:

1. Executive Summary

2. Key Points

3. Important Findings

4. Final Conclusion

Document:

{text}
"""

    return ask_gemini(prompt)