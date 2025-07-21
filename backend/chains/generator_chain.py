from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from utils.llm_loader import get_llm

prompt = PromptTemplate.from_template("Generate a detailed response for: {input}")
generator_chain = LLMChain(llm=get_llm(), prompt=prompt)
