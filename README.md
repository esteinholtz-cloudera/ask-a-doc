# ask-a-doc
learn from a book by asking it questions! By using the ChatGPT API and tainting your dialogue with a book, manual or any text corpus, you can interactively ask questions to the text

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
Update the .env file with your Open API key and DBPATH where you want to store your embeddings

```. ./.env```

Will get your environment in place and then...:

```FLASK_APP=UI.py flask run```

will fire up the UI. Connect your browser and ask away!

If you want to ingest more corpuses (corpi??), just change the DBPATH first, then your old stuff will not be overwritten and you can reuse it in the future
