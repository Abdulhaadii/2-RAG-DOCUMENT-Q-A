# 📄 RAG Document Q&A with LangChain & OpenAI

A Streamlit web application that allows you to upload PDF documents and ask questions about their content using **Retrieval-Augmented Generation (RAG)** with **LangChain** and **OpenAI** embeddings.

---

## 🚀 Features

- Upload multiple PDF files at once.
- Automatically split documents into chunks for efficient retrieval.
- Generate embeddings using OpenAI API.
- Perform semantic search over uploaded documents.
- Ask questions and get answers directly from your PDFs.

---

## 🛠️ Technologies Used

- **Python 3.13+**
- [Streamlit](https://streamlit.io/) – Web app framework
- [LangChain](https://www.langchain.com/) – LLM integrations & vector storage
- [FAISS](https://github.com/facebookresearch/faiss) – Vector similarity search
- [OpenAI API](https://platform.openai.com/) – Embeddings generation
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management

---

## 💾 Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd <repo-folder>
Create a virtual environment (recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file in the root folder with:

ini
Copy code
OPENAI_API_KEY=your_openai_api_key_here
🖥️ Usage
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Upload your PDF files using the file uploader.

Wait for the app to process the documents and create a vector store.

Enter your query in the text input box.

Get answers retrieved directly from your documents.

📁 Project Structure
bash
Copy code
.
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── uploaded_pdfs/         # Temporary folder for uploaded PDFs
├── README.md              # Project documentation
└── .env                   # Environment variables
⚡ Notes
Make sure your OpenAI API key is valid and has sufficient usage quota.

This project uses FAISS for vector storage, which allows fast similarity search over large document collections.

The document chunks are split using a chunk size of 1000 with an overlap of 200 characters for better context retention.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
LangChain Documentation

Streamlit Documentation

OpenAI API
