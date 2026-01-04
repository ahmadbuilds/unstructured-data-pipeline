from langchain_ollama import ChatOllama

def create_ollama_instance(model_name:str="llama3.1:8b",temperature:float=0):
    model=ChatOllama(
        model=model_name,
        temperature=temperature,
    )
    return model