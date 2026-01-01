# step1_chunking.py

# -------------------------------
# 1) Read the file
# -------------------------------
with open("employee_handbook_clean.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Total text length:", len(text))

# -------------------------------
# 2) Split text into chunks
# -------------------------------
chunk_size = 500   # number of characters per chunk
overlap = 50       # overlap between chunks

chunks = []
start = 0
while start < len(text):
    end = start + chunk_size
    chunk = text[start:end]
    chunks.append(chunk)
    start = end - overlap

print("Number of chunks:", len(chunks))

# -------------------------------
# 3) Add metadata to each chunk
# -------------------------------
documents = []

for chunk in chunks:
    doc = {
        "text": chunk,
        "metadata": {
            "source": "employee_handbook",
            "department": "HR",
            "access_level": "employee",
            "topic": "general"  # can refine later to leave/benefits/remote
        }
    }
    documents.append(doc)

# -------------------------------
# 4) Save the result as JSON
# -------------------------------
import json

with open("employee_handbook_chunks.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, ensure_ascii=False, indent=2)

print("JSON file created: employee_handbook_chunks.json")
print("Sample first chunk:")
print(documents[0])
