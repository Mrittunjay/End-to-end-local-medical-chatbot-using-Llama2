"""
The find_packages() and setup() function are from the setuptools library.
'find_packages' automatically discovers all packages and sub-packages in the
project directory, while 'setup' is used to specify the metadata and configuration 
for your package. 

-e . in requirements.txt installs all the package in 'editable' mode. The change to 
the source code of the package will be immediately reflected in the environment
without needing to install the package.
"""

from setuptools import find_packages, setup

setup(name = 'Medic-Chat-LLM',
      version = '0.0.0',
      author = 'Sipan Pal',
      author_email = 'paul.mrittunjoy777@gmail.com',
      packages = find_packages(),
      install_requires = [])