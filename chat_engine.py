import os
import streamlit as st
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

persist_dir = "db"

def get_response(query):
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    vectordb = Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
        retriever=retriever,
        chain_type="stuff"
    )
    return qa.run(query)