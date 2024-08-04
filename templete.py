# This file will create the folder structure for the 
# project deployment

import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s)')

list_dir = [
    "src/__init__.py",
    "src/halper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chatbot.html"
]

# Creating all the files and folders in the above list
for filepath in list_dir:
    filepath = Path(filepath)
    
    # seperating directories and files from the file path
    directory, file = os.path.split(filepath)

    # Creating the directory
    if directory != "":
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Created directory: {directory}")
    # Creating the file
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"{file} file already exists")
    




