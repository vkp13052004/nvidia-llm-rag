from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from utils.llm_loader import get_llm

llm = get_llm()
memory = ConversationBufferMemory()
basic_chat_chain = ConversationChain(llm=llm, memory=memory)
