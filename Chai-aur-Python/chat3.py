import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenRouter(
    model="openai/gpt-4.1-mini",
    temperature=0, #Softmax adjust kr skte ho
    max_tokens=500, # max_tokens used in the output is limited to 200 only 
)

system_prompt = """
You are an ai assistant who is expert in breaking down complex problems
and then resolve the user query 

For the given user input,analyse the input and break down the problems step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse,you think,you again think for several times and then return an output with explanations and then finally you validate the output as well before giving final result.



Example:
Input : What is 2 + 2.
Output : {{ step : "analyse",content : "Alright! The user is interested in maths query and he is asking a basic arithmetic expression."}}
Output : {{step:"think",content:"To perform the addition I must go from Left to right and following all the operands ."}}
Output:{{step : "output",content:"4"}}
Output:{{step:"validation",content:"The result is 4"}}



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