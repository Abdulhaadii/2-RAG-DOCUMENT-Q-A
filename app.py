# -----------------------------
# Imports
# -----------------------------
import os
from dotenv import load_dotenv
import streamlit as st

# LangChain imports (v1.2.6+)
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFDirectoryLoader

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Streamlit app
# -----------------------------
st.set_page_config(page_title="RAG Document Q&A", layout="wide")
st.title("📄 RAG Document Q&A with LangChain & OpenAI")

# -----------------------------
# Upload PDFs
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload PDF files", type="pdf", accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    # Save uploaded files to a temp folder
    temp_folder = "uploaded_pdfs"
    os.makedirs(temp_folder, exist_ok=True)

    for file in uploaded_files:
        with open(os.path.join(temp_folder, file.name), "wb") as f:
            f.write(file.getbuffer())

    # -----------------------------
    # Load PDF documents
    # -----------------------------
    loader = PyPDFDirectoryLoader(temp_folder)
    documents = loader.load()

    st.write(f"Total pages loaded: {len(documents)}")

    # -----------------------------
    # Split documents into chunks
    # -----------------------------
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)
    st.write(f"Total chunks created: {len(docs)}")

    # -----------------------------
    # Create embeddings
    # -----------------------------
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(docs, embeddings)

    st.success("Vector store created successfully!")

    # -----------------------------
    # Q&A interface
    # -----------------------------
    query = st.text_input("Ask a question about your documents:")

    if query:
        # Retrieve relevant chunks
        results = vectorstore.similarity_search(query, k=3)
        answer = "\n\n".join([doc.page_content for doc in results])
        st.subheader("Answer from documents:")
        st.write(answer)
