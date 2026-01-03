import os 
from config import FILE_TYPES

def validate_empty_path(path):
    if len(path)==0:
        return False
    
def validate_file_type(path):
    chunks=path.split(".")
    if chunks[-1]==FILE_TYPES and len(chunks)!=1:
        return True
    else:
        print("only .txt files are supported")
        return False
    
def validate_file_existence(path):
    if os.path.isfile(path):
        return True
    else:
        print("file does not exist. Invalid Path!")
        return False
