from pathlib import Path
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from utils import Config

def index_files():
    """
    Loads and processes the PDF documents, splits them into chunks, 
    and creates the vector store.
    """
    config = Config()
    config.initialize()

    embeddings = config.get_embeddings()

    if embeddings is None:
        raise ValueError("Embeddings not found")
    
    folderPath = Path.cwd() / "data"

    loader = PyPDFDirectoryLoader(folderPath)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./research_papers_db")


if __name__ == "__main__":
    index_files()