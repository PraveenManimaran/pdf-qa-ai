import streamlit as st
import openai
import os
from pdf_utils import extract_text_from_pdf
import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Streamlit App UI
st.set_page_config(page_title="📄 PDF Q&A AI", layout="wide")
st.title("📄 PDF Q&A AI: Ask Questions from Your Documents")

# Set OpenAI API Key
api_key = st.text_input("🔑 Enter your OpenAI API key", type="password")

if api_key:
    openai.api_key = api_key
else:
    st.warning("⚠️ Please enter an API key to use the app.")


# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")
# embedding_function = OpenAIEmbeddings()
embedding_function = OpenAIEmbeddings(openai_api_key=api_key)

vector_store = Chroma(collection_name="pdf_embeddings", embedding_function=embedding_function, client=chroma_client)


# File Upload
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    with st.spinner("Extracting text..."):
        extracted_text = extract_text_from_pdf(uploaded_file)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_text(extracted_text)

        # Store embeddings
        try:
            vector_store.add_texts(chunks)
            st.success("✅ PDF uploaded and processed successfully!")
        except Exception as e:
            st.error(f"❌ Error storing embeddings: {e}")

# Question Input
question = st.text_input("💬 Ask a Question")
if st.button("🔎 Get Answer") and question:
    retriever = vector_store.as_retriever()
    # qa = RetrievalQA.from_chain_type(
    #     llm=ChatOpenAI(model="gpt-4"),
    #     retriever=retriever
    # )
    qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4", openai_api_key=api_key),
    retriever=retriever
    )
    with st.spinner("Fetching answer..."):
        answer = qa.run(question)
        st.write("**📝 Answer:**")
        st.info(answer)
