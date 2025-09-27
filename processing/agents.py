import os
import requests

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")
MODEL = os.getenv("OPENROUTER_MODEL", "gpt-4o-mini")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    # 👇 required by OpenRouter
    "HTTP-Referer": "http://localhost:3000",   # or your GitHub repo URL
    "X-Title": "agentic-ai-boilerplate"
}

def summarize(docs):
    content = "\n\n".join([d.page_content for d in docs])

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Summarize these documents."},
            {"role": "user", "content": content}
        ]
    }

    resp = requests.post(f"{BASE_URL}/chat/completions", headers=HEADERS, json=payload)

    if resp.status_code != 200:
        raise RuntimeError(f"OpenRouter error: {resp.status_code} {resp.text}")

    return resp.json()["choices"][0]["message"]["content"]

def answer_question(vectordb, question):
    docs = vectordb.as_retriever().get_relevant_documents(question)
    context = "\n\n".join([d.page_content for d in docs])

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Answer the question using the context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    }

    resp = requests.post(f"{BASE_URL}/chat/completions", headers=HEADERS, json=payload)

    if resp.status_code != 200:
        raise RuntimeError(f"OpenRouter error: {resp.status_code} {resp.text}")

    return resp.json()["choices"][0]["message"]["content"]
