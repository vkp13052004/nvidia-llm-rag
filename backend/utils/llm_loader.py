from langchain.llms import ChatNVIDIA

def get_llm():
    return ChatNVIDIA(model="meta/llama3-8b-instruct", temperature=0.7)
