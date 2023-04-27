# ask-a-doc
Learn from a book by asking it questions! By using the ChatGPT API and tainting your dialogue with a book, manual or any text corpus, you can interactively ask questions to the text.

What is the caveat? You have to get an Open API key. But it is very cheap to use in my opinion.

## How to use
1. Create Embeddings from your documents - just running a python script
2. Fire up the local webserver UI
3. Ask your questions to the docs in a chatbot format

## Detailed (yeah) setup
Prerequisite: You need to have python installed. 

Install dependencies:

```dependencies.sh ```

to get the necessary python modules

Then, Get an Open AI API key
Update the .env file with your Open API key and DBPATH, which is where you want to store your embeddings. 

```. ./.env```

## Ingestion
This is the step where you encode your text corpus as embeddings.
And What is embeddings? A fancy word for "vector representations of the meaning of a certain chunk of text".

In this version, only PDFs are supported. But due to the large stack of file formats available in the langchain library, this can be easily remedied.
Shoutout (pull request) if you want to add a format or two.

```python ingest-cli.py <root_directory_for_texts>```

## Run!

Will get your environment in place and then...:

```FLASK_APP=UI.py flask run```

will fire up the UI. Connect your browser and ask away!

If you want to ingest more corpuses (corpi??), just change the DBPATH first, then your old stuff will not be overwritten and you can reuse it in the future
