import faiss
import pickle
import numpy as np
import json
from sentence_transformers import SentenceTransformer

# Load embedding model (local, offline)
model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("company_index.faiss")

with open("company_chunks.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)


# User query
query = "How many sick leave days do employees have?"

# Create embedding for the query
query_embedding = model.encode([query]).astype("float32")

# Search in FAISS
k = 5
distances, indices = index.search(query_embedding, k)

# Display results
print("Query:", query)
print("\nTop relevant chunks:\n")

for rank, idx in enumerate(indices[0]):
    print(f"Result {rank + 1}:")
    print(metadata[idx])
    print("-" * 50)
