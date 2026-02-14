from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

import os ,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.ingest import load_document
from app.rag_pipe import build_rag_chain
from app.embeddings import create_vector_store

from fastapi import UploadFile, File
import shutil


app = FastAPI(title="RAG GenAI Platform")

qa_chain = None
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class Query(BaseModel):
    question: str

@app.on_event("startup")
def startup():
    global qa_chain

    try:
        qa_chain = build_rag_chain()
    except:
        qa_chain = None

@app.post('/ingest')
async def ingest(file: UploadFile =File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR,file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file,buffer)

        documents = load_document(file_path)
        create_vector_store(documents)

        qa_chain = build_rag_chain()

        return {"status": "Document indexed successfully",
                "file name": file.filename
                }
    
    except Exception as e:
        print("INGEST ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during ingestion: {str(e)}"
        )


@app.post('/query')
def query(query: Query):

    if qa_chain is None:

        raise HTTPException(
            status_code=503,
            detail="RAG chain is not available. Please ingest documents first."
            )

    answer = qa_chain.run(query.question)

    return {"answer": answer}
