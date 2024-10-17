import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI


class ChromaInterface:
    def __init__(self):
        pass

    def create_chunks(self) -> list:

        # Create chunks from PDF
        file_path = "docs/bitcoin-whitepaper.pdf"

        loader = PyPDFLoader(file_path)
        document = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=200, chunk_overlap=100
        )
        chunks = text_splitter.split_documents(document)

        print(f"{len(chunks)} chunks were created.\n")

        return chunks

    def upsert_chunks(self) -> None:
        """Stores document chunks on Chroma.

        Args:
            chunks (list): List of dictionaries, each representing a document chunk from Bitcoin's whitepaper.
        """
        chunks = self.create_chunks()

        chroma_client = chromadb.Client()

        collection = chroma_client.get_or_create_collection(name="bitcoin-chatbot")
        collection.upsert(
            documents=[chunks[i].page_content for i in range(len(chunks))],
            ids=[f"{i}" for i in range(len(chunks))],
        )

        print(f"{len(chunks)} documents were stored on Chroma.\n")

    def query(self, query: str) -> list:
        """Queries Chroma for documents that match the given query.

        Args:
            query (str): The query/question to search for.

        Returns:
            list: List of dictionaries, each representing a document chunk that matches the query.
        """
        chroma_client = chromadb.Client()

        collection = chroma_client.get_or_create_collection(name="bitcoin-chatbot")

        results = collection.query(query_texts=[query], n_results=1)

        return results

chroma_interface = ChromaInterface()
chroma_interface.upsert_chunks()