# from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore


# Creating a loader to load pdf data
def load_pdf_data(data_path):
    """
    Loads PDF documents from a specified directory and return the loaded documents.
    
    Args:
        data_path (str): The path to the directory containing PDF file/files.
    
    Returns:
        list: A list of loaded documents from the pdf files.
    """
    # Creating a directory loader instance to load files from the given path
    loader = DirectoryLoader(
        path=data_path,
        glob="*.pdf",               # Matching file formet
        loader_cls=PyPDFLoader,     # Class to use for loading PDF file
        show_progress=True,         
        use_multithreading=True     # Use multithreading while loading documents
    )
    docs = loader.load()
    return docs


# Splitting the data into chunks
def get_text_chunks(data):
    """
    Splits the given text data into chunks of a specified size with overlap.
    
    Args:
        data (list): A list of documents to be split into cunks
    
    Returns:
        list: A list of text chunks obtained by splitting the input data
    """
    # Initialize the text splitter class
    extracted_chunks = RecursiveCharacterTextSplitter(
        chunk_size=500,         # Size of each chunk (number of characters)
        chunk_overlap=30,       # Number of characters to overlap between consecutive chunks.
    )
    # Get the split text/chunks using split_documents
    doc_split = extracted_chunks.split_documents(data)
    return doc_split


# Initializing the embedding model
def get_hugging_face_embeddings():
    """
    Initializes and returns an embedding model from Hugging Face's Sentence Transformers.

    Returns:
        HuggingFaceEmbeddings: An instance of the HuggingFaceEmbeddings class initialized with a specific model.
    """
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding


# Function to create a vector store in pinecone
def get_pinecone_vectorestore(doc_chunks, embedding, index_name, pc):
    """
    Create or retrive a Pinecone vector store based on the provided index name.
    
    Args:
    - doc_chunks (list): A list of document chunks to be indexed
    - embedding (object): The embedding model used for vectorizing the document chunks
    - index_name (str): The name of the Pinecone instance to use or create vector database
    
    Returns:
    - PineconeVectorStore: An instance of PineconeVectorStore, either newly created or retrieved
    """
    # Getting the vector details
    vector_details = pc.Index(index_name).describe_index_stats()
    print(vector_details)
    if vector_details['total_vector_count'] == 0:
        vectorstore = PineconeVectorStore.from_documents(doc_chunks, embedding=embedding, index_name=index_name)
    else:
        vectorstore = PineconeVectorStore(index_name=index_name, embedding=embedding)
    return vectorstore


# Function to print results cleanly
def print_result(result):
    if 'result' in result:
        print("Result: ", result['result'])