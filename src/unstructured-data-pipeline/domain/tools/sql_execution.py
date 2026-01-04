from langchain.tools import tool
import sqlite3
from config import GENERATED_SCHEMA_PATH

@tool
def manipulating_DBTable(query:str)->str:
    "Creating new Tables and for Inserting and updating new Data into the Table"
    try:
        connection_object=sqlite3.connect(GENERATED_SCHEMA_PATH)
        cur=connection_object.cursor()
        res=cur.execute(query)
        return str(res.fetchall())
    except:
        return "Failed to create the Database table"
    finally:
        connection_object.close()
