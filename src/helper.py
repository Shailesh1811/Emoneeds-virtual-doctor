# Extract Data from PDF file
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    return loader.load()


# Filter to minimal docs
from typing import List
from langchain.schema import Document

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects
    containing only 'source' in metadata and the original page_content.
    """

    minimal_docs: List[Document] = []

    for doc in docs:
        src = doc.metadata.get("source")

        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )

    return minimal_docs


# Split the documents into smaller chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_split(minimal_docs):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )

    texts_chunk = text_splitter.split_documents(minimal_docs)

    return texts_chunk


# Download and load HuggingFace Embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def download_hugging_face_embeddings():

    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )

    return embeddings




