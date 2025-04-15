import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from document_loader import load_documents

CHROMA_DIR  = "memory/chroma_db"

def create_vectore_store(persist_dir=CHROMA_DIR):
    docs = load_documents()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
         documents=docs, 
        embedding=embeddings, 
        persist_directory=persist_dir
    )
    vectorstore.persist()

    return vectorstore

def load_vector_store(persist_dir=CHROMA_DIR):
    if os.path.exists(CHROMA_DIR):
        print(f"{persist_dir} path exists")

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = Chroma(
            embedding_function=embeddings,
            persist_directory=persist_dir
        )
    else:
        print(f"{persist_dir} path does not exist")
        vectorstore = create_vectore_store()

    return vectorstore

def get_similar_docs(vectorstore, query, k=3):

    return vectorstore.similarity_search(query, k=k)

