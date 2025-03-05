from flask import Flask, request, jsonify
import openai
import os
from pdf_utils import extract_text_from_pdf
import chromadb
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI

from langchain.text_splitter import RecursiveCharacterTextSplitter

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 This allows frontend requests from other origins

# Load API Key
openai.api_key = os.getenv("OPENAI_API_KEY")


# Initialize ChromaDB for storing PDF embeddings
chroma_client = chromadb.PersistentClient(path="chroma_db")
embedding_function = OpenAIEmbeddings()
vector_store = Chroma(collection_name="pdf_embeddings", embedding_function=embedding_function, client=chroma_client)


@app.route("/upload", methods=["POST"])
def upload_pdf():
    """Handles PDF uploads, extracts text, stores in ChromaDB."""
    if "pdf" not in request.files:
        print("❌ No PDF file received!")  # Debug Log
        return jsonify({"error": "No PDF file uploaded"}), 400

    pdf_file = request.files["pdf"]
    print(f"✅ Received file: {pdf_file.filename}")  # Debug Log

    extracted_text = extract_text_from_pdf(pdf_file)
    if not extracted_text:
        print("❌ No text extracted from PDF!")  # Debug Log
        return jsonify({"error": "Failed to extract text"}), 500

    print(f"📄 Extracted text (first 500 chars): {extracted_text[:500]}")  # Debug Log

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(extracted_text)
    print(f"🔹 Total Chunks Created: {len(chunks)}")  # Debug Log

    # Store embeddings
    try:
        vector_store.add_texts(chunks)
        print("✅ Successfully stored embeddings in ChromaDB!")  # Debug Log
    except Exception as e:
        print(f"❌ Error storing embeddings: {e}")  # Debug Log
        return jsonify({"error": "Failed to store embeddings"}), 500

    return jsonify({"message": "PDF uploaded and processed successfully."})


@app.route("/ask", methods=["POST"])
def ask_question():
    """Handles user queries using the stored document context."""
    data = request.get_json()
    user_question = data.get("question", "")

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    # Use LangChain's RetrievalQA to get answers
    retriever = vector_store.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4"),
        retriever=retriever
    )

    answer = qa.run(user_question)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
