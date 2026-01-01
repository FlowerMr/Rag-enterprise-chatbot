import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load chunks
with open("company_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Total chunks combined: {len(chunks)}")

# Load local embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
texts = [chunk["text"] for chunk in chunks]
embeddings = model.encode(texts, show_progress_bar=True)

embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "company_index.faiss")

print("FAISS index rebuilt successfully.")
