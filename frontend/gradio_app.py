import gradio as gr
import requests

def chat_with_llm(prompt):
    response = requests.post(
        "http://localhost:8000/basic_chat/invoke",
        json={"input": prompt}
    )
    return response.json().get("output", "No response.")

iface = gr.Interface(fn=chat_with_llm, inputs="text", outputs="text", title="Chat with NVIDIA LLM")
iface.launch()
