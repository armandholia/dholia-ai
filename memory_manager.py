import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

persist_dir = "db"

def process_files(files):
    documents = []
    for file in files:
        path = f"data/{file.name}"
        with open(path, "wb") as f:
            f.write(file.getbuffer())

        if file.name.endswith(".pdf"):
            loader = PyPDFLoader(path)
        else:
            loader = TextLoader(path)

        documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    vectordb = Chroma.from_documents(
        docs,
        embedding=OpenAIEmbeddings(),
        persist_directory=persist_dir
    )
    vectordb.persist()
