from fastapi import FastAPI
from langserve import add_routes
from chains.basic_chat import basic_chat_chain
from chains.retriever_chain import retriever_chain
from chains.generator_chain import generator_chain

app = FastAPI()
add_routes(app, basic_chat_chain, path="/basic_chat")
add_routes(app, retriever_chain, path="/retriever")
add_routes(app, generator_chain, path="/generator")
