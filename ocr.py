import pytesseract
#import os
#import sys

async def create(path, lang = 'eng'):
    try:
        return pytesseract.image_to_string(path, lang = lang)
    except:
        return "Unable to process file"