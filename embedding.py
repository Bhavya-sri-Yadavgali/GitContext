from sentence_transformers import SentenceTransformer

from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I forgot my password",
    "How can I reset my password?",
    "The weather is beautiful today",
    "How do I authenticate a user?",
    "JWT tokens are used for authentication."
]

embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print(sentence)
    print("Vector length:", len(embedding))
    print("First 5 values:", embedding[:5])
    print()

similarity = cos_sim(embeddings, embeddings)

print(similarity)