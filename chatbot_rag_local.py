# chatbot_rag_local.py
import os
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.service_context import ServiceContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def build_rag_chatbot():
    llm = Ollama(model="llama3", request_timeout=120.0)
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    try:
        documents = SimpleDirectoryReader("./data").load_data()
    except ValueError:
        print("Error: './data' directory empty or missing. Add your docs and retry.")
        return None

    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
        chunk_size=512
    )

    db = chromadb.PersistentClient(path="./chroma_db")
    chroma_collection = db.get_or_create_collection("domain_specific_docs")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    print("Creating vector index... this may take a while.")
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        service_context=service_context
    )
    print("Index created.")
    chat_engine = index.as_chat_engine(
        chat_mode="context",
        system_prompt="Answer based only on the provided documents."
    )
    return chat_engine

def start_chat_cli(chat_engine):
    if not chat_engine:
        return
    print("Local RAG Chatbot initialized. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        response = chat_engine.chat(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    engine = build_rag_chatbot()
    start_chat_cli(engine)
