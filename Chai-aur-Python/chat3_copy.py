import os
import json
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

load_dotenv()

model = ChatOpenRouter(
    model="openai/gpt-4.1-mini",
    temperature=0, #Softmax adjust kr skte ho
    max_tokens=500, # max_tokens used in the output is limited to 200 only 
    response_format={
        "type": "json_object"
    }
)

system_prompt = """
You are an ai assistant who is expert in breaking down complex problems
and then resolve the user query 

For the given user input,analyse the input and break down the problems step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse,you think,you again think for several times and then return an output with explanations and then finally you validate the output as well before giving final result.

Follow these steps in sequence that is "analyse","think","output","validate","result" .

Rules : 
1. Follow the strict JSON output as per the output schema .
2. Always perform one step at a time and wait for next input
3. carefully analyse the user query

Output Format : 
{{ step : "string", content : "string" }}


Example:
Input : What is 2 + 2.
Output : {{ step : "analyse",content : "Alright! The user is interested in maths query and he is asking a basic arithmetic expression."}}
Output : {{step:"think",content:"To perform the addition I must go from Left to right and following all the operands ."}}
Output:{{step : "output",content:"4"}}
Output:{{step:"validate",content:"seems like 4 is correct ans for 2 + 2"}}
Output:{{step:"result",content:"2+2 = 4 and that is calculated by adding all the numbers."}}


"""

messages=[
   SystemMessage(content=system_prompt)
    
]

query=input("> ")
messages.append( HumanMessage(
        content=query
    ))

while True:
    response=model.invoke(messages)

    parsed_response=json.loads(response.content)
    messages.append(AIMessage(content=json.dumps(parsed_response)))


    if parsed_response.get("step") != "result":
        print(f"AI : {parsed_response.get('content')}")
        continue

    print(f"Final Answer : {parsed_response.get('content')}")

    break