import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# Yes, your prompt is doing few-shot prompting. 
# Few-shot prompting means you give the model multiple examples of input → output behavior before giving the actual query.
# It teaches the model the expected format, style, and logic.
# Basically it is teaching or training the model for the type of output you want from it.


model = ChatOpenRouter(
    model="openai/gpt-4.1-mini",
    temperature=0, #Softmax adjust kr skte ho
    max_tokens=200, # max_tokens used in the output is limited to 200 only 
)

system_prompt = """You are an ai assistant who is specialized in maths.You should not answer any query that is not related to maths. 
For a given math problem, you should first think step by step and then provide the solution.

Example:
Input : 2+2
Output : 2+2 is 4 which is calculated by adding 2 with 2.

Input:3*10
Output : 3*10 is 30 which is calculated by multiplying 3 with 10.
FunFact you can also multiply 10*3 and the answer will be the same.

Input:Why is sky blue??
Output :Bruh ? You alright? Is this a math query.??

"""

messages = [
    SystemMessage(
        content=system_prompt
    ),
    HumanMessage(
        content="What is a mobile phone."
    )
]

response = model.invoke(messages)

print(response.content)