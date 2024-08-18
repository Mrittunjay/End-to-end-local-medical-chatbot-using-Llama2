from flask import Flask, render_template, jsonify, request
from src_code.halper import *
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src_code.prompt import *
from langchain.prompts import PromptTemplate
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
# from langchain.llms import CTransformers
from langchain_community.llms import CTransformers
import torch
import os

app = Flask(__name__)

# Loading the env file
load_dotenv()

# Load document
pdf_docs = load_pdf_data("data")

# Getting document chunks
doc_chunks = get_text_chunks(pdf_docs)

# Accessing api key and index from environ
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_INDEX_NAME = os.environ.get('PINECONE_INDEX_NAME')

embeddings = get_hugging_face_embeddings()

# Initializing the pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = PINECONE_INDEX_NAME
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

""" 
Getting vectors from pinecode if vectros already uploaded
or upload the vectors in vector db.
"""
vectorstore = get_pinecone_vectorestore(doc_chunks=doc_chunks, 
                                        embedding=embeddings, 
                                        index_name=PINECONE_INDEX_NAME,
                                        pc=pc)

# Creating a prompt template
prompt_template = PromptTemplate(template=llm_prompt, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": prompt_template}

# Creating device agnostic code
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Model running on {device}")
# Instantiate llama-2 llm model
# llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q4_0.bin",
#                     model_type="llama",
#                     device=device,
#                     config={'max_new_tokens':400,
#                             'temperature': 0.5}
#                     )
llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q2_K.bin",
                    model_type="llama",
                    device=device,
                    config={'max_new_tokens':200,
                            'temperature': 0.3}
                    )

# Creating question-ans obj
qa_obj = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# user_input = input("Ask your query related to general medicine and disease: ")
# result = qa_obj.invoke({"query": user_input})
# print_result(result)


# Flask default route
@app.route("/")
def index():
    return render_template('chatbot.html')

@app.route("/bot", methods=["GET", "POST"])
def bot():
    query = request.form["messageText"]
    print(query)
    result = qa_obj.invoke({"query": query})
    return jsonify({"result": result["result"]})


# Initializing flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
