import streamlit as st
import requests

BACKEND_URL = 'http://127.0.0.1:8000'

st.set_page_config(page_title="RAG GenAI Platform", layout="centered")

st.title("RAG GenAI Platform")

st.header("Upload PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

#file upload and ingest
if uploaded_file:

    with st.spinner('uploading and processing...'):

        files = {'file':uploaded_file.getvalue()}
        response = requests.post(f"{BACKEND_URL}/ingest", files=files)

    if response.status_code == 200:
        st.success("Document indexed successfully!")
    else:
        st.error(f"Error: {response.text}")

#querying
st.header("Ask a question")

question = st.text_input('Enter your question here')

if st.button("Get Answer"):

    if question.strip()=="":
        st.warning("Please enter a question.")
    else:
        with st.spinner('Getting answer...'):

            response = requests.post(f'{BACKEND_URL}/query',json={'question':question})

        if response.status_code == 200:
            answer = response.json().get('answer')

            st.markdown("**Answer:**")
            st.write(answer)