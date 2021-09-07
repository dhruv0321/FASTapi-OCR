# FASTapi-OCR

Using REST API and tesseract OCR - take image from user and return text data

# Task
The goal of the task is to build an API that extracts text from a text image data and returns.

# SOLUTION

### Technology used
    - Python 3.9
    - FastAPI (https://fastapi.tiangolo.com/)
    - tesseract OCR
 
### Download and Install Required tools
    - sudo apt install tesseract
    - Postman : https://www.postman.com/downloads/
    - Python (3.9.6) : https://www.python.org/downloads/

### Required packages for python
    - pytesseract : used to connect pyhton with tesseract
    - FastAPI : to create REST API
    - uvicorn : to host the asgi server

#### Commands to install required packages
    - pip install -r requirements.txt

### Operations that can be performed with API
    - get list of all the api available 
    - get list of all the documents avaiable to parse
    - parse a document to text
    - add image to be parsed
        - to add image use the body field

### Instructions to get this working
    - make a virtual environment and install all the python packages 
      using the following commands
        - pip install virtualenv
        - virtualenv env
        - source myvenv/bin/activate
        - pip install -r requirement.txt
    - Install postman and open the postman.json file to get access to all the API    
    - " uvicorn main:app --reload " to run the server
