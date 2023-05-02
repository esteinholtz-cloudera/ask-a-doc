from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

def ask_model(query):

    DBPATH=os.getenv('DBPATH')

    #db = Chroma.from_documents(texts, embeddings)
    db = Chroma(persist_directory=DBPATH, embedding_function=OpenAIEmbeddings())

    retriever = db.as_retriever()
    from langchain.chains.retrieval_qa.base import RetrievalQA
    from langchain.llms.openai import OpenAI

    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)

    return (qa.run(query))

