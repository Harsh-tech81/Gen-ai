import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents="Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall",
)

embedding_vector = response.embeddings[0].values

print("Embedding created successfully!")
print("Dimensions:", len(embedding_vector))
print("Fully Embedding Models", embedding_vector)
