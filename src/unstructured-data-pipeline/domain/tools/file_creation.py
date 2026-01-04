from langchain.tools import tool
import os 
from config import GENERATED_SCHEMA_PATH


@tool
def check_DBfile_existence()->bool:
    "Check if the file exist or not"
    if os.path.isfile(GENERATED_SCHEMA_PATH):
        return True
    return False

@tool
def db_file_creation()->str:
    "Create a new Database file"
    try:
        with open(GENERATED_SCHEMA_PATH,"w") as file:
            return "Database File Created Successfully"
    except:
        return "Failed to create database file"
    finally:
        file.close()