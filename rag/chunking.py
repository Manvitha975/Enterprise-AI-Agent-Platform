"""
Chunking Module

Splits long text into overlapping chunks
for Retrieval-Augmented Generation (RAG).
"""


def split_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[str]:
    """
    Splits text into overlapping chunks.

    Args:
        text: Complete document text
        chunk_size: Number of characters per chunk
        overlap: Number of overlapping characters

    Returns:
        List of text chunks
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks