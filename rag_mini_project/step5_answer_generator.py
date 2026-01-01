import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from llm_formatter import format_with_llm

# Load embedding model (MUST be same as step3)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index (correct filename)
index = faiss.read_index("company_index.faiss")

# Load chunks + metadata (correct filename)
with open("employee_handbook_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

# Question
question = "How many sick leave days do employees have?"

# Embed query
query_embedding = model.encode([question]).astype("float32")

# Search
k = 5
distances, indices = index.search(query_embedding, k)

best_chunk = None
best_score = float("inf")

for i, idx in enumerate(indices[0]):
    chunk = chunks[idx]

    # Access control
    if chunk["metadata"].get("access_level") != "employee":
        continue

    if distances[0][i] < best_score:
        best_score = distances[0][i]
        best_chunk = chunk["text"]

if best_chunk is None:
    print("Answer:\nAccess denied or no relevant information found.")
    exit()

# Confidence
confidence = float(np.exp(-best_score))

# LLM formatting (Ollama)
answer = format_with_llm(best_chunk, question)

if confidence < 0.4:
    answer = "I'm not fully confident about the answer. Please contact HR for accurate information."

print("Question:", question)
print("\nAnswer:\n", answer)
