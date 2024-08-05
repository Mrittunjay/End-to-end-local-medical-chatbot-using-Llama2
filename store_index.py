from src_code.halper import load_pdf_data, get_text_chunks, get_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv  # Used to access the secret key for pinecone present in .env fiele
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os



# Loading the env file
load_dotenv()

# Accessing api key and index from environ
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_INDEX_NAME = os.environ.get('PINECONE_INDEX_NAME')

# Extracting data from pdf file
pdf_docs = load_pdf_data("data")

# Getting data chunks from the loaded pdf
doc_chunks = get_text_chunks(pdf_docs)

# Loading the embeddings
minilm_embedding = get_hugging_face_embeddings()

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = PINECONE_INDEX_NAME
# Create Pinecone index if already not present in pinecone webpage
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        ) 
    ) 



