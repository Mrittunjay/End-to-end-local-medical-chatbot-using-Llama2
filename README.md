# End-to-end-local-medical-chatbot-using-Llama2

## Steps to run the project

```bash
conda create -n medic-chatbot python=3.8 -y
```

```bash
conda activate medic-chatbot
```

```bash
pip install -r requirements.txt
```

## The model will be slow if running on CPU. If you have NVIDIA GPU you can go with the following steps
### (optinal) Install cuda enabled torch run the following command:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
# Note: Make sure you have cuda toolkit 11.8 installed (Run "nvcc --version" to check).


## Run the following command to create the folder structure(For model deplyment in web) it will also create the .env file.
```bash
python template.py
```

## Create a Pinecone account on https://app.pinecone.io/ 
## Now create a pinecone api key and add it to .env file, also provide a name for the pinecone instance as follows:
Example: 
PINECONE_API_KEY = "00000000-0000-00cd-ab00-000000000000"

PINECONE_INDEX_NAME = "example_index_name"


## For the first time the code will create a pinecode instance with the index name that you have provided, and update the chunk vectors to the vector-DB (This will take quite some time during the first run)


## Download the required model .bin files and place in the model folder.
### For more information and links refer to model/instruction.txt file. 

## (Optional)If you encounter issues with CTransformers library while loading the 2 bit llama model, then upgrade the library
```bash
pip install --upgrade CTransformers
```

## Run the Chatbot with following command
```bash
python app.py
```

## Open the chat bot at 
http://localhost:8080/

## Note: You can use any template of your choice for the fornt-end UI of the chatbot. Add the HTML file in 
### templates folder and CSS file in static folder. 


## Average rasponse time : 20 Seconds (If CUDA GPU is used. With CPU response time will be more)


## Ongoing work:
### Significantly reduce bot response time.
### Use more source data to run the model.   
