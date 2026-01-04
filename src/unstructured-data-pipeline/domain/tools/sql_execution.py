from langchain.tools import tool
import sqlite3
from config import GENERATED_SCHEMA_PATH

@tool
def manipulating_DBTable(query:str)->str:
    """
    Executes SQL statements to create tables, insert, or update data.
    Returns a success/failure message.
    """
    try:
        connection_object=sqlite3.connect(GENERATED_SCHEMA_PATH)
        cur=connection_object.cursor()
        
        with connection_object:
            cur.executescript(query)
        return  "SQL executed successfully"
    except sqlite3.Error as e:
        return f"Failed to execute query:{e}"
    finally:
        connection_object.close()
