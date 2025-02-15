Vector PDF Search using Astra DB and Google AI

This project is a PDF document retrieval and question-answering system that leverages Astra DB for cloud storage and Google AI's SentenceTransformer model for semantic search. Users can input queries, and the system will return the most relevant text chunk from the uploaded PDF documents.

Features-
•	Extracts text from PDFs using PyPDF2.
•	Stores text chunks in Astra DB.
•	Converts both stored texts and user queries into semantic embeddings using Google AI's all-MiniLM-L6-v2 model.
•	Finds and returns the most relevant text chunk based on cosine similarity.
Technologies Used-
•	Python: Core language for development.
•	Astra DB: Cloud database for storing PDF text chunks.
•	LangChain: For text splitting and database integration.
•	SentenceTransformer: Embedding and semantic search using Google AI’s pre-trained model.
•	PyPDF2: Extracts text from PDF files.
•	Torch: Used by SentenceTransformer for embedding and similarity computation.
Getting Started
1.	Clone the Repository
https://github.com/sudhakar1298/vector-pdf-search-with-astra-google-ai.git

2.	Set Up Environment
python -m venv env
env\Scripts\activate
3.	Install Dependencies
pip install astrapy langchain PyPDF2 sentence-transformers torch
4.	Configure Astra DB
ASTRA_DB_APPLICATION_TOKEN = "YOUR_ASTRA_DB_APPLICATION_TOKEN"
ASTRA_DB_API_ENDPOINT = "YOUR_ASTRA_DB_API_ENDPOINT"
ASTRA_DB_KEYSPACE = "YOUR_ASTRA_DB_KEYSPACE"
5.	Run the Program
python llm.py
6.	Interact with the System
You will be prompted to enter questions based on the content of the PDF. Type your question and receive the best-matching text as a response. Type quit to exit.

Project Structure
.
├── main.py            # Main script for the project
├── example.pdf              # Sample PDF file for text extraction
├── README.md          # Project documentation
└── requirements.txt   

Demo-
QUESTION: "What is the capital of France?"
ANSWER: "The capital of France is Paris."

To-Do / Future Improvements
•	Add support for multiple PDFs.
•	Integrate a web interface for easier user interaction.
•	Enhance answer formatting and relevancy scoring.
•	Add more AI models for advanced text understanding.

