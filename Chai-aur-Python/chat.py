import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()
# Zero-shot prompting means This is already zero-shot prompting

# You give the model a task/instruction without providing any examples of how to solve it.
model = ChatOpenRouter(
    model="openai/gpt-4.1-mini",
    temperature=0,
    max_tokens=1024,
)

response = model.invoke(
    "What is the capital of France?"
)

print(response.content)