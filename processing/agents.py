# processing/agents.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize(docs):
    content = "\n\n".join([d.page_content for d in docs])

    resp = client.chat.completions.create(
        model=os.getenv("MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": "Summarize these documents."},
            {"role": "user", "content": content}
        ]
    )
    return resp.choices[0].message.content

def answer_question(vectordb, question):
    retriever = vectordb.as_retriever()
    docs = retriever.invoke(question)   # ✅ replaces get_relevant_documents
    context = "\n\n".join([d.page_content for d in docs])

    resp = client.chat.completions.create(
        model=os.getenv("MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": "Answer the question using the context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
    )
    return resp.choices[0].message.content

