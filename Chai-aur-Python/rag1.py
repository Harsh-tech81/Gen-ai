
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
load_dotenv()
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage

pdf_path = Path(__file__).parent/"RAG_Test_Document.pdf"

loader = PyPDFLoader(file_path=pdf_path)
documents = loader.load()
# print(documents)

model = ChatOpenRouter(
    model="openai/gpt-4.1-mini",
    temperature=0, #Softmax adjust kr skte ho
    max_tokens=200, # max_tokens used in the output is limited to 200 only 
)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

split_docs=text_splitter.split_documents(documents)
# print(len(documents))
# print(len(split_docs))

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview",
api_key=os.getenv("GEMINI_API_KEY")
)

# vectorstore = QdrantVectorStore.from_documents(
#     documents=[],
#     embedding=embeddings,
#     url="http://localhost:6333",
#     collection_name="learning_langChain",

# )


# vectorstore.add_documents(documents=split_docs)


# now we have to retrieve the data on user's Query 

vectorstore = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_langChain",
)

query = "What is this PDF is about..??"

results = vectorstore.similarity_search(query)

# print(results[0].page_content)

# print("Vector store created successfully")

system_prompt = """

You are a helpful assistant.
Use the retrieved data to answer the query.
If the answer is not in the retrieved data, say so.

"""

messages = [
    SystemMessage(
        content=system_prompt
    ),
    HumanMessage(
        content=query+f"\n\nRetrieved data: {results[0].page_content}"
    )
]

response = model.invoke(messages)

print(response.content)


