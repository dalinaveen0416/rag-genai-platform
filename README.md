## RAG GenAI Platform

This project is a production-style Retrieval-Augmented Generation (RAG) platform that I built to allow users to interact with their own documents using a Large Language Model. The main idea behind this project was to understand how modern GenAI systems combine document retrieval and LLMs to generate accurate, context-aware responses instead of relying only on the model’s internal knowledge.

In this system, users can upload documents, ask questions, and receive answers grounded in their document content. Behind the scenes, the application converts documents into embeddings, stores them in a vector database, retrieves relevant information when a question is asked, and then sends that context to the LLM for response generation.

This project helped me gain hands-on experience in building real-world GenAI applications using FastAPI, LangChain, FAISS, Hugging Face embeddings, and Groq.

## What this platform can do

Using this platform, you can:

Upload documents

Ask questions about your documents

Get context-aware answers

Perform semantic search

Build your own document-based AI assistant

The responses are generated based only on the uploaded content, which improves accuracy and reduces hallucinations.

## How the system works internally

When a document is uploaded, the system first extracts the text and splits it into smaller chunks. Each chunk is then converted into embeddings using a Hugging Face embedding model.

These embeddings are stored in a FAISS vector database.

When a question is asked, the system converts the question into an embedding and searches FAISS to find the most relevant document chunks.

Those retrieved chunks are then sent along with the question to Groq’s LLaMA3 model using LangChain, and the model generates a response based on that context.

This entire process is called Retrieval-Augmented Generation (RAG).

## Setting up the Groq API key

This project uses Groq’s LLaMA3 model to generate responses.

Before running the project, you need to get a Groq API key.

You can create one from:

https://console.groq.com/

After getting your API key, create a .env file in the project root folder and add:

GROQ_API_KEY=your_api_key_here


The application will automatically read this key when it starts.

This approach keeps the API key secure and prevents exposing it in the code.

📁 Project structure
rag-genai-platform/
│
├── app/
│   ├── config.py        # Loads environment variables and configuration
│   ├── embeddings.py    # Embedding model setup
│   ├── ingest.py        # Document loading and chunking
│   ├── rag_pipe.py      # Retrieval and LLM pipeline
│   ├── main.py          # FastAPI backend
│
├── ui.py                # Streamlit user interface
├── requirements.txt     # Dependencies
├── README.md

## Installation and setup

First, clone the repository:

git clone https://github.com/yourusername/rag-genai-platform.git

cd rag-genai-platform


Create virtual environment:

python -m venv env


Activate environment:

Windows:

env\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Create .env file and add your Groq API key.

## Running the backend

Start FastAPI server:

uvicorn app.main:app --reload


Open in browser:

http://localhost:8000/docs


This opens the API interface where you can test endpoints.

## Running the user interface

Start Streamlit interface:

streamlit run ui.py


Open:

http://localhost:8501


From here, you can upload documents and ask questions.

## Example workflow

Typical usage looks like this:

Start backend

Start Streamlit UI

Upload document

Ask question

Receive grounded response

## Technologies used

I built this project using:

Python

FastAPI

Streamlit

LangChain

Groq (LLaMA3)

Hugging Face Embeddings

FAISS

Sentence Transformers

## Why I built this project

I built this project to understand how production-style GenAI systems work beyond simple chatbot examples.

Through this project, I learned how to:

Build Retrieval-Augmented Generation pipelines

Work with vector databases

Integrate LLM APIs into backend systems

Improve response accuracy using semantic search

Design real-world AI applications

This project helped me understand the complete workflow of document-based GenAI systems.


Once the backend and UI are running, you can upload any document and ask questions such as:

Summarize the document

What skills are mentioned

Explain specific topics from document

The system will retrieve relevant content and generate responses.

## Future improvements

In the future, I plan to extend this project by adding:

Multi-user support

Monitoring dashboard

Evaluation and hallucination detection

Cloud deployment

Authentication system

## Author

Naveen Dali
Python Developer | Generative AI Engineer

## Final note

This project demonstrates how to build a real-world GenAI application using Retrieval-Augmented Generation, vector databases, and LLM integration.

It combines backend development, AI pipelines, and user interface into one complete system.
