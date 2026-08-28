
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
load_dotenv()

pdf_path = Path(__file__).parent/"RAG_Test_Document.pdf"

loader = PyPDFLoader(file_path=pdf_path)
documents = loader.load()
# print(documents)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

split_docs=text_splitter.split_documents(documents)
# print(len(documents))
# print(len(split_docs))

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",
api_key=os.getenv("GEMINI_API_KEY")
)

vectorstore = QdrantVectorStore.from_documents(
    documents=[],
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_langChain",

)


vectorstore.add_documents(documents=split_docs)
print("Vector store created successfully")