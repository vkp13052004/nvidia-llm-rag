from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from utils.llm_loader import get_llm

retriever = FAISS.load_local("vector_index", HuggingFaceEmbeddings())
retriever_chain = RetrievalQA.from_chain_type(
    llm=get_llm(), chain_type="stuff", retriever=retriever
)
