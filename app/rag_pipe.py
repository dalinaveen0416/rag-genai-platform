from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.embeddings import load_vector_store
from app.config import settings

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
       You are an AI assistant for document question answering.

       rules:
       - Use only given context.
       -if the answer is not in the context, say 'Not found in the document'.
       -keep answer concise.
       -do not HALLUCINATE.
       -try to give informatio in bullet points if the answer is long.
Context:{context}
Question: {question}

Answer in this format.

<your answer here>

source:
<short reference from context>
"""
)
def build_rag_chain():

    llm = ChatGroq(
        model=settings.LLM_MODEL,
        api_key=settings.GROQ_API_KEY,
        temperature=0.2
    )

    db = load_vector_store()

    retriever = db.as_retriever(search_type='similarity', search_kwargs={'k': 3})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type = 'stuff',
        chain_type_kwargs={
            'prompt': RAG_PROMPT
        }
    )

    return qa_chain
