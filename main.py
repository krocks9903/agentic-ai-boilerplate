from dotenv import load_dotenv
load_dotenv()

from ingest.loaders import load_documents
from storage.vector_store import create_vectorstore
from processing.agents import summarize, answer_question

def main():
    docs = load_documents("sample_docs/")
    if not docs:
        print("⚠️ No documents found in sample_docs/. Please add a PDF or DOCX.")
        return

    vectordb = create_vectorstore(docs)

    summary = summarize(docs)
    print("\n--- SUMMARY ---\n", summary)

    q = "What are the payment terms?"
    ans = answer_question(vectordb, q)
    print(f"\nQ: {q}\nA: {ans}")

if __name__ == "__main__":
    main()
