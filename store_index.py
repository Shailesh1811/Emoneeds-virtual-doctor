from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    return loader.load()

extracted_data = load_pdf_files("data")

print(len(extracted_data))

extracted_data = load_pdf_files("data")

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


minimal_docs = filter_to_minimal_docs(extracted_data)

minimal_docs = filter_to_minimal_docs(extracted_data)

print(type(extracted_data))
print(type(minimal_docs))



# Split the documents into smaller chunks

from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_split(minimal_docs):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )

    texts_chunk = text_splitter.split_documents(minimal_docs)

    return texts_chunk


# Call the function
texts_chunk = text_split(minimal_docs)

print(f"Number of chunks: {len(texts_chunk)}")



# Download and load HuggingFace Embeddings

from langchain_community.embeddings import HuggingFaceEmbeddings


def download_embeddings():

    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )

    return embeddings


# Call function

embedding = download_embeddings()
print("Embedding model loaded successfully")


from dotenv import load_dotenv
import os
load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY



import os
from langchain_groq import ChatGroq

chatModel = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)


from pinecone import Pinecone
pinecone_api_key = PINECONE_API_KEY

PC = Pinecone(api_key=pinecone_api_key)


from pinecone import Pinecone, ServerlessSpec

index_name = "emoneeds-index"

# Create Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Get list of indexes
existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

# Create index if not exists
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Connect to index
index = pc.Index(index_name)

print("Pinecone connected successfully")


from langchain_pinecone import PineconeVectorStore

docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunk,
    embedding=embedding,
    index_name=index_name
)

# Load Existing index

from langchain_pinecone import PineconeVectorStore

# Embed each chunk and upsert the embeddings into your Pinecone index.

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

