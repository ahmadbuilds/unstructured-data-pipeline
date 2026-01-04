from langchain.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from config import GENERATED_SCHEMA_PATH

template = ChatPromptTemplate.from_messages([
    SystemMessage(
        "You are an expert data engineer. "
        "Your task is to generate valid SQLite SQL statements that update existing tables "
        "or create them if they do not exist. "
        "Using the provided content from multiple input files, create database tables "
        "with column names exactly as defined in {main_schema}. "
        "Define foreign key columns and relationships exactly as specified in {foreign_schema}. "
        "Infer appropriate SQLite data types, create all required tables, "
        "and generate executable SQL statements for table creation and data insertion. "
        "Do not add extra columns or tables beyond the provided schemas. "
        "Return only executable SQLite SQL. Do not include explanations, comments, or markdown."
    )
])

