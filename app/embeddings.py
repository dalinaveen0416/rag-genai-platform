#this file contains the code for creating embeddings and storing them in a faiss vector database.

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.config import settings

def create_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
    db =FAISS.from_documents(documents,embeddings)

    #saving the database
    db.save_local(settings.VECTOR_DB_PATH)



def load_vector_store():

    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

    return FAISS.load_local(
        settings.VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
                            )