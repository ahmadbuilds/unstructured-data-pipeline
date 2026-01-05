import os 
from domain.validators.file_naming import validate_empty_path,validate_file_type,validate_file_existence
from typing import Set
from concurrent.futures import ThreadPoolExecutor
from config import OPTIMAL_NUMBER_THREADS,FILE_TYPES

files=set()
files_content=set()
def Thread_Validation_Function(path:str):
    #validating the file paths
    if validate_empty_path(path) and validate_file_type(path) and validate_file_existence(path):
        files.add(path)

def Thread_File_Reader(path:str):
    #reading the content of file
    try:
        with open(path,"r") as file:
            content=file.read()
            files_content.add(content)
    except:
        print(f"Failed to read Content of file:{path}")
    finally:
        file.close()

def read_files(file_paths:list[str])->Set[str]:
    #Splitting the Files Reading into Worker Threads
    with ThreadPoolExecutor(max_workers=OPTIMAL_NUMBER_THREADS) as e:
        for path in file_paths:
            e.submit(Thread_Validation_Function,path)

     
    #reading the content of Valid files
    with ThreadPoolExecutor(max_workers=OPTIMAL_NUMBER_THREADS) as e:
        for valid_files in files:
            e.submit(Thread_File_Reader,valid_files)

    return files_content
    