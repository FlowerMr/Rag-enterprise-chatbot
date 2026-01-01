import subprocess

def format_with_llm(context, question):
    prompt = f"""
You are an internal company assistant.
Answer ONLY using the context below.
If the context does not contain the answer, say: "I don't have enough information."

Context:
{context}

Question:
{question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
