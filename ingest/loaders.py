from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
import os

def load_documents(path: str):
    docs = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(full_path).load())
        elif file.endswith(".docx"):
            docs.extend(Docx2txtLoader(full_path).load())
    return docs
