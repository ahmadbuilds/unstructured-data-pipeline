from domain.prompts.llm_instructions import template
from domain.schema.invoice import Invoice,ItemDetails
from domain.schema.llm_output import response_output
from domain.tools.file_creation import db_file_creation,check_DBfile_existence
from domain.tools.sql_execution import manipulating_DBTable
from infrastructure.llm_providers.llama_provider import create_ollama_instance
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.checkpoint.memory import InMemorySaver

checkPointer=InMemorySaver()

def create_agent_instance():
    agent=create_agent(
        model=create_ollama_instance(),
        system_prompt=template,
        tools=[db_file_creation,check_DBfile_existence,manipulating_DBTable],
        response_format=ToolStrategy(response_output),
        checkpointer=checkPointer
    )

    return agent