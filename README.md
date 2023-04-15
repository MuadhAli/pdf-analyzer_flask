# Project Name

This is a Flask web application that uses the LangChain library for text analysis and search.

## Installation

1. Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate


2. Install dependencies:
pip install langchain
pip install flask
pip install unstructured
pip install tiktoken
pip install unstructured[local-inference]
pip install chromadb



3. Clone the repository and navigate to the project directory:
for http
git clone https://github.com/MuadhAli/pdf-analyzer_flask.git

for ssh
git@github.com:MuadhAli/pdf-analyzer_flask.git
cd pdf-analyzer_flask



4. Run the Flask app:
python ./app.py



## Usage

1. Access the web application in your browser at `http://127.0.0.1:5000/`.

2. Upload a PDF file using the file upload form.

3. Enter a search query in the provided input field and click the "Search" button.

4. The app will search for documents in the PDF file that match the query and display the results on the webpage.

5. You can customize the functionality and behavior of the app by modifying the Flask app code in `app.py` and the templates in the `templates` directory as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bug fixes, improvements, or new features.

## Acknowledgements

This project was built using the LangChain library, which provides text analysis and search capabilities.

## Contact

For questions or inquiries, please contact [https://www.instagram.com/muadhalikhan/?next=%2F].





