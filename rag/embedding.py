"""
Embedding Module

Converts text chunks into embeddings
using Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(chunks: list[str]):
    """
    Creates embeddings for text chunks.

    Args:
        chunks: List of text chunks

    Returns:
        List of embeddings
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings