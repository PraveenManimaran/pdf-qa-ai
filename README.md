# 📄 PDF Q&A AI: Ask Questions from Your Documents  

A **Retrieval-Augmented Generation (RAG)-based AI application** that allows users to upload PDFs and ask questions, powered by **OpenAI's GPT-4, LangChain, and ChromaDB**.  

---

## **🚀 Features**
✅ Upload PDFs and extract text  
✅ Store document embeddings in **ChromaDB**  
✅ Use **GPT-4** to answer questions based on the document content  
✅ User-friendly **Streamlit UI**  
✅ Secure API Key input (No hardcoded keys)  

---

## **📦 Required Dependencies**
### **🔹 Python Packages**
This project uses the following Python libraries:  
- **Streamlit** → For the web UI  
- **OpenAI** → GPT-4 API for Q&A  
- **LangChain** → For retrieval-augmented generation (RAG)  
- **ChromaDB** → To store and retrieve embeddings  
- **PyMuPDF (`pymupdf`)** → To extract text from PDFs  
- **tiktoken** → For efficient tokenization  
- **Flask** → If you plan to run a separate backend  

---

## **🛠️ Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/PraveenManimaran/pdf-qa-ai.git
cd pdf-qa-ai
