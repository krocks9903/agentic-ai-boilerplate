# storage/vector_store.py
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def create_vectorstore(docs):
    """
    Create a FAISS vector store using OpenAI embeddings.
    """
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",   # ✅ efficient + cheap
        api_key=os.getenv("OPENAI_API_KEY")
    )

    return FAISS.from_documents(docs, embeddings)
