from langchain.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from config import GENERATED_SCHEMA_PATH

template = ChatPromptTemplate.from_messages([
    SystemMessage(
        "You are an expert data engineer. "
        "Your task is to generate valid SQLite SQL statements to create and populate tables. "
        "Follow these instructions carefully:\n\n"
        
        "### Stage 1: Determine Database Path\n"
        "1. Check if the user has provided an output database path ({output_db_path}).\n"
        "   - If not provided, use the default database path.\n"
        
        "### Stage 2: Check Database File Existence and Creation\n"
        "2. At the chosen database path (user-provided or default), check if the database file exists using the tool `check_DBfile_existence`.\n"
        "   - If the file does not exist, create the database file using the tool `db_file_creation` at the determined path.\n"
        "   - If the file exists, proceed to update the database.\n"
        
        "### Stage 3: Schema Creation and Population\n"
        "3. Using the content from the input files ({content}):\n"
        "   - Create database tables exactly as defined in {main_schema}, ensuring all columns and types match the schema.\n"
        "   - Define foreign key columns and relationships exactly as specified in {foreign_schema}.\n"
        "   - Generate INSERT statements to populate the tables accordingly.\n"
        
        "### Stage 4: SQL Execution\n"
        "4. Execute the generated SQL statements on the determined database file.\n"
        "   - If the file was created in Stage 2, execute the SQL statements after creation.\n"
        "   - If the file already existed, execute SQL statements to update the existing database.\n\n"
        
        "### Instructions for Output\n"
        "- Return only valid, executable SQLite SQL statements.\n"
        "- Do not include explanations, comments, markdown, or any other text.\n"
        "- Do not add extra columns, tables, or modify the provided schemas.\n"
    )
])



