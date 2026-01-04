from langchain_ollama import ChatOllama

def create_ollama_instance(model_name:str="llama3.1:8b",Temperature:float=0.5):
    model=ChatOllama(
        model=model_name,
        temperature=Temperature,
    )
    return model