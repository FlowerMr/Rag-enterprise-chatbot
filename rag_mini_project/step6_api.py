from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load model and data
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("company_index.faiss")

with open("company_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

class Query(BaseModel):
    question: str
    k: int = 3

@app.post("/ask")
def ask(query: Query):
    q_emb = model.encode([query.question]).astype("float32")
    distances, indices = index.search(q_emb, query.k)

    results = []
    for i, d in zip(indices[0], distances[0]):
        results.append({
            "text": chunks[i]["text"],
            "metadata": chunks[i]["metadata"],
            "distance": float(d)
        })

    best = results[0]["text"].split("\n")
    clean = [l for l in best if l.strip() and not l.startswith("===")]
    answer = " ".join(clean[:4])

    return {
        "question": query.question,
        "answer": answer,
        "sources": results
    }
