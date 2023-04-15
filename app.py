from flask import Flask, render_template, request
import os
import tempfile
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredPDFLoader

os.environ['OPENAI_API_KEY'] = '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'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def analyze_pdf():
    uploaded_file = request.files['file']

    if uploaded_file.filename != '':
        # Save the uploaded file to a temporary file on disk
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file.flush()

            # Load the PDF from the temporary file
            loader = UnstructuredPDFLoader(temp_file.name)
            documents = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)
            embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
            docsearch = Chroma.from_documents(texts, embeddings)
            qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch)

            query = request.form['query']

            result = qa({"query": query})

            return render_template('index.html', result=result['result'])
    else:
        return render_template('index.html', error_message="Please upload a valid PDF file.")

if __name__ == '__main__':
    app.run(debug=True)
