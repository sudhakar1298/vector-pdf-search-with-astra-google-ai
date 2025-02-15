import os
from astrapy import DataAPIClient
from langchain_community.vectorstores.cassandra import Cassandra
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util

ASTRA_DB_APPLICATION_TOKEN = "Your TOKEN"
ASTRA_DB_API_ENDPOINT = "Your API ENDPOINT"
ASTRA_DB_KEYSPACE = "Your Keyspace Name"

client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)
database0 = client.get_database(ASTRA_DB_API_ENDPOINT)
collection0 = database0.get_collection("Your Collection Name")

print("Connected to Astra DB")

collection0.delete_all()


pdf_path = "Example.pdf" #better to store the file and code file in the same page
if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"PDF file '{pdf_path}' not found!")

pdfreader = PdfReader(pdf_path)
raw_text = "\n".join(page.extract_text() for page in pdfreader.pages if page.extract_text())

text_splitter = CharacterTextSplitter(separator="\n", chunk_size=800, chunk_overlap=200, length_function=len)
texts = text_splitter.split_text(raw_text)

for item in texts:
    collection0.insert_one({"content": item})

print(f"Inserted {len(texts)} text chunks into the vector store.")

stored_texts = [doc["content"] for doc in collection0.find()]
print(f"fetched {len(stored_texts)} documents from Astra DB.")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
stored_embeddings = [embedding_model.encode(text, convert_to_tensor=True) for text in stored_texts]

while True:
    query_text = input("\nEnter your question (or type 'quit' to exit): ").strip()
    if query_text.lower() == "quit":
        print("Thank You")
        break
    if not query_text:
        continue

    print(f"\nQUESTION: \"{query_text}\"")

    query_embedding = embedding_model.encode(query_text, convert_to_tensor=True)
    similarities = [util.pytorch_cos_sim(query_embedding, stored_embedding).item() for stored_embedding in stored_embeddings]
    
    best_match_index = similarities.index(max(similarities))
    best_match_text = stored_texts[best_match_index]

    query_embedding = embedding_model.encode(query_text, convert_to_tensor=True)
    similarities = [util.pytorch_cos_sim(query_embedding, stored_embedding).item() for stored_embedding in stored_embeddings]

    best_match_index = similarities.index(max(similarities))
    best_match_text = stored_texts[best_match_index]

    formatted_text = best_match_text.replace('\n', ' ')
    print(f"ANSWER: {formatted_text}")
