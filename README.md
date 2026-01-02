# 🧠 Enterprise RAG Chatbot (Local & Secure)

This project implements a **production-style Retrieval-Augmented Generation (RAG) system**<img width="2752" height="1536" alt="unnamed" src="https://github.com/user-attachments/assets/f383241b-7c0e-4b86-bf9b-aa46160baa39" />

designed for internal enterprise knowledge bases (HR, IT, Finance).

It focuses on **security, role-awareness, and scalability**, not demo-level chatbots.

---

## 🚀 Features

- Document ingestion (PDF → clean text)
- Semantic chunking
- Vector embeddings (Sentence Transformers)
- FAISS vector database
- Role-aware metadata (department, access level)
- Confidence-based fallback answers
- FastAPI backend (enterprise-ready)
- Fully local (no OpenAI dependency)

---

## 🧱 Architecture Overview


User Query
↓
Embedding Model
↓
FAISS Vector Search
↓
Top-K Relevant Chunks
↓
Access Control Check
↓
Answer Generation
↓
API Response

---

## 📁 Project Structure

rag_mini_project/
│
├── step1_chunking.py # Text chunking
├── step2_remote_chunks.py # Metadata + department tagging
├── step3_embeddings.py # Vector embeddings + FAISS index
├── step4_query.py # Semantic retrieval
├── step5_answer_generator.py # Clean answer + confidence
├── step6_api.py # FastAPI backend
│
├── employee_handbook_clean.txt
├── remote_work_policy.txt
│
├── company_chunks.json
├── company_index.faiss
│
└── README.md



---

## 🧪 How to Run

### Install dependencies
```bash
pip install sentence-transformers faiss-cpu fastapi uvicorn

Run Api
python -m uvicorn step6_api:app --port 8081
🔐 Enterprise Considerations

Role-based filtering (HR / IT / Finance)

Access-level aware retrieval

Hallucination reduction via RAG

Confidence threshold with rule-based fallback

🎯 Use Case

Internal company chatbot:

HR policies

Remote work rules

Benefits and employment terms

Secure internal Q&A

📌 Status

✅ Functional
✅ Local
✅ Interview-ready
🚧 UI & Auth can be added
