# Vector PDF Search using Astra DB and Google AI

This project is a **PDF document retrieval and question-answering system** that leverages **Astra DB** for cloud storage and **Google AI's SentenceTransformer** model for semantic search. Users can input queries, and the system will return the most relevant text chunk from the uploaded PDF documents.

---

## 🛠️ **Features**

- Extracts text from PDFs using `PyPDF2`.
- Stores text chunks in **Astra DB**.
- Converts both stored texts and user queries into semantic embeddings using **Google AI's all-MiniLM-L6-v2** model.
- Finds and returns the most relevant text chunk based on **cosine similarity**.

---

## 🔧 **Technologies Used**

- **Python**: Core language for development.
- **Astra DB**: Cloud database for storing PDF text chunks.
- **LangChain**: For text splitting and database integration.
- **SentenceTransformer**: Embedding and semantic search using Google AI’s pre-trained model.
- **PyPDF2**: Extracts text from PDF files.
- **Torch**: Used by SentenceTransformer for embedding and similarity computation.

---

## 🚀 **Getting Started**

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/vector-pdf-search-using-astra-db-google-ai.git
cd vector-pdf-search-using-astra-db-google-ai
