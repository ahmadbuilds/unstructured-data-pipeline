from domain.prompts.llm_instructions import template
from domain.schema.invoice import Invoice,ItemDetails
from domain.schema.llm_output import response_output
from domain.tools.file_creation import db_file_creation,check_DBfile_existence
from domain.tools.sql_execution import manipulating_DBTable
from infrastructure.llm_providers.llama_provider import create_ollama_instance
from langchain.agents import create_react_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.checkpoint.memory import InMemorySaver
from domain.schema.invoice import Invoice,ItemDetails

checkPointer=InMemorySaver()

def create_agent_instance():
    agent=create_react_agent(
        model=create_ollama_instance(),
        system_prompt=template,
        tools=[db_file_creation,check_DBfile_existence,manipulating_DBTable],
        response_format=ToolStrategy(response_output),
        checkpointer=checkPointer
    )

    return agent


def format_template(main_schema:Invoice,foreign_schema:ItemDetails,content:str,output_db_path:str=None)->str:
    formatted_template=template.format(
        main_schema=main_schema,
        foreign_schema=foreign_schema,
        content=content,
        output_db_path=output_db_path,
    )
    return formatted_template