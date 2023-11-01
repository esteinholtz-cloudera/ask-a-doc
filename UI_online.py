from flask import Flask, render_template, request
from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
import os

from langchain.document_loaders import TextLoader

#initialize
LOAD_TEXT=str((os.getenv('LOAD_TEXT')))
if os.path.isfile(LOAD_TEXT):
    loader = TextLoader(LOAD_TEXT)
    from langchain.indexes import VectorstoreIndexCreator
    index = VectorstoreIndexCreator().from_loaders([loader])

app = Flask(__name__)
app.config["SECRET_KEY"] = "i år kommer julen tidigt"  # Replace with your own secret key
csrf = CSRFProtect(app)

@app.route('/')
def index_html():
    return render_template('index.html')

#Submit
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    return index.query(user_input)

@app.route('/list_directories', methods=['GET'])
def list_directories():
    base_path = 'persistence/'  # Replace with the base directory on your Document
    directories = os.listdir(base_path)
    return jsonify(directories)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print (file.filename)
    print (file.name)
    return 'File uploaded successfully!'

@app.route('/ingest_directories', methods=['POST'])
def ingest_directories():
    ingest_dir1 = request.form['ingest_dir1']
    ingest_dir2 = request.form['ingest_dir2']
    
    # Do something with ingest_dir1 and ingest_dir2
    return 'Ingesting directories: {} and {}'.format(ingest_dir1, ingest_dir2)

@app.route('/load_directory', methods=['POST'])
def load_directory():
    load_dir = request.form['load_dir']
    # Do something with load_dir
    return 'Loading directory: {}'.format(load_dir)

if __name__ == '__main__':
    app.run(debug=True)
