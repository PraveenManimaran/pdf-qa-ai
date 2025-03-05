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
git clone https://github.com/PraveenManimaran/pdf-qa-ai.git
cd pdf-qa-ai

### **2️⃣ Create a Virtual Environment**
**Mac/Linux:**
python3 -m venv venv
source venv/bin/activate

**Windows:**
python -m venv venv
venv\Scripts\activate

### **3️⃣ Install Dependencies**
pip install -r requirements.txt

### **🔑 4️⃣ Set Up OpenAI API Key**
Since we don't hardcode API keys, you need to set it as an environment variable:

**Mac/Linux:**
export OPENAI_API_KEY="your-api-key-here"

**Windows (PowerShell):**
$env:OPENAI_API_KEY="your-api-key-here"

OR you can enter the key manually in the Streamlit UI.

### **🚀 5️⃣Run the Application**
streamlit run app_streamlit.py





