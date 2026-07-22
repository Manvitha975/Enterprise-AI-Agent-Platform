from rag.chunking import split_text

text = """
Artificial Intelligence is transforming every industry.

Machine Learning is a subset of AI.

Deep Learning is a subset of Machine Learning.

Neural Networks power modern AI systems.

Large Language Models are based on Transformer architectures.
""" * 20

chunks = split_text(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}")

    print(chunk[:200])

    print("-" * 50)