from dotenv import load_dotenv
import os

load_dotenv()

GENERATED_SCHEMA_PATH=os.getenv("FILES_STORAGE")
FILE_TYPES=os.getenv("FILE_TYPES_ALLOWED")