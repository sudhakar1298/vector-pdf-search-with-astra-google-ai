Here's the full content formatted as a `README.md` file:

```markdown
# 📄 Vector PDF Search using Astra DB and Google AI

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
```

---

### 2. **Set Up Environment**
Ensure you have Python installed. You can create a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

---

### 3. **Install Dependencies**
Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
torch
langchain
pydantic
sentence-transformers
PyPDF2
cassandra-driver
```

---

### 4. **Set Up Astra DB**
1. Create a free **Astra DB** account at [Astra DB](https://www.datastax.com/astra).
2. Create a new database and download the **secure connect bundle** (a `.zip` file).
3. Extract the secure connect bundle and note the directory path.
4. Set an environment variable or create a `.env` file in the root directory with the following content:

   ```env
   ASTRA_DB_SECURE_CONNECT_PATH=/path/to/your/secure-connect-database-name.zip
   ```

5. Use the following sample code to connect to Astra DB:

   ```python
   from cassandra.cluster import Cluster
   from cassandra.auth import PlainTextAuthProvider

   auth_provider = PlainTextAuthProvider(client_id, client_secret)
   cluster = Cluster(cloud={'secure_connect_bundle': '/path/to/your/secure-connect-database-name.zip'})
   session = cluster.connect()
   session.set_keyspace('your_keyspace_name')
   ```

---

### 5. **Run the Application**
After setting up the environment and configuration, run the application:

```bash
python main.py
```

This will start the semantic search service. You can now upload PDFs and input queries.

---

### 6. **Testing the System**
1. Upload a sample PDF.
2. Enter a question related to the PDF content in the input field.
3. The system will process the query, compute embeddings, and return the most relevant text chunk.

---

### 7. **Deployment (Optional)**

- **Local Deployment**: Use `Flask` or `FastAPI` to create a web interface for local deployment.
- **Cloud Deployment**: You can deploy the application to **Heroku**, **AWS**, **Azure**, or **Google Cloud**.
- **Containerization**: Use the following `Dockerfile` for easy containerization:

   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   CMD ["python", "main.py"]
   ```

   To build and run the Docker container:

   ```bash
   docker build -t vector-pdf-search .
   docker run -p 5000:5000 vector-pdf-search
   ```

---

### 8. **Troubleshooting Tips**
- Ensure Astra DB credentials are correct and accessible.
- Check for any errors during PDF text extraction or embedding generation.
- Confirm all required libraries are installed.

---

## 📜 **License**
This project is licensed under the [MIT License](LICENSE).

---

## 💬 **Contact**
For any questions or feedback, feel free to reach out at [your-email@example.com].

```
