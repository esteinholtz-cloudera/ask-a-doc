def ingest(text_corpus, target_dir, chunk_size=1000, chunk_overlap=0): 

    # %%
    from langchain.document_loaders import TextLoader
    loader = TextLoader(text_corpus)

    documents = loader.load()

    # %%
    from langchain.text_splitter import CharacterTextSplitter
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    # %%
    from langchain.embeddings import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()

    # %%
    from langchain.vectorstores import Chroma

    #db = Chroma.from_documents(texts, embeddings)
    db = Chroma(persist_directory=str(target_dir), embedding_function=OpenAIEmbeddings())

    return db