from typing import Text
from fastapi import FastAPI, UploadFile
from fastapi.param_functions import File
import ocr
import os
import shutil

app = FastAPI()
FilePath = os.getcwd() + "/files/"

@app.get("/")
def read_root():
    available_api = {
        'GET' : {
            'get doc list' : '/get_doc_list',
            'parse document' : '/parse/<document_id>'
            },
        'POST' : {
            'add docs' : '/add_doc'
        }
        }
    return {'available api' : available_api}

@app.get("/get_doc_list")
def doc_list():
    file_names = []
    for file in os.listdir("files"):
        file_names.append(file)
    return {"file_names" : file_names}

@app.get("/parse/{doc_id}")
async def parse (doc_id) :
    text = await ocr.create(FilePath + doc_id)
    return {"filename" : doc_id,"text" : text}

@app.post("/add_doc")
async def add_doc(image : UploadFile = File(...)):
    try:
        temp_file = os.path.join(FilePath, image.filename)
        with open(temp_file,"wb") as buffer:
            shutil.copyfileobj(image.file,buffer)
        return {"response ": "File added successfully"}
    except:
        return {"response ": "Could not add file"}