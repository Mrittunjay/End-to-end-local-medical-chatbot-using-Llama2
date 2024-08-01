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

###To install cuda enabled torch run the following command:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
Note: Make sure you have cuda toolkit 11.8 installed (Run "nvcc --version" to check).