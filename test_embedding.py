from rag.embedding import create_embeddings

chunks = [
    "Machine Learning is a subset of AI.",
    "Deep Learning uses Neural Networks.",
    "FastAPI is used for backend APIs."
]

embeddings = create_embeddings(chunks)

print("Total Embeddings:", len(embeddings))

print()

print("Embedding Dimension:")

print(len(embeddings[0]))

print()

print(embeddings[0][:10])