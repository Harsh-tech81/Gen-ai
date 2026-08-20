import os
from dotenv import load_dotenv
import json
import requests
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


load_dotenv()

def get_weather(city: str):
    # To do an actual API calling to find the weather condition.

    print(f"Tool called : {city}")
    url =f"https://wttr.in/{city}?format=%C+%t"
    response=requests.get(url)

    if(response.status_code==200):
        return f"The weather in {city} is {response.text}"
    else:
        return "Error : Could not fetch weather data"

import subprocess

def run_command(command):
    print(f"Tool called : run_command({command})")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout if result.stdout else "Command executed successfully (no output)."
        else:
            return f"Error (Exit Code {result.returncode}): {result.stderr}"
    except Exception as e:
        return f"Exception occurred while running command: {str(e)}"

# print(run_command("dir"))

available_tools = {
    "get_weather": {
        "fn" : get_weather,
        "description" : "Takes a city name as an input and returns the current weather for the city"
    },
    "run_command":{
        "fn":run_command,
        "description":"Runs a command on the system"
    }

}

model = ChatOpenRouter(
    model="openai/gpt-4.1-mini",
    temperature=0,
    max_tokens=500,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    response_format={
        "type": "json_object"
    }
)


system_prompt = """
You are an helpful AI Assistant who is specialized in resolving user query.

You work on start,plan,action,observe mode.
For the given user query and available tools, plan the step by step execution, based on the planning, select the relevant tool from the available tool. and based on the tool selection you can perform an action to call the tool.Wait for the observation and based on the observation from the tool call resolve the user query.


Rules : 
- Follow the output in JSON format.
- Always perform one step at a time and wait for next input.
- carefully analyse the user query.


Output JSON Format :
{{
"step":"string",
"content":"string",
"function":"The name of the function if the step is action"
"input":"The input parameter for the function."

}}

Available Tools : 
- get_weather: Takes a city name as an input and returns the current weather for this city.
- run_command: Takes a command as an input and runs it on the Windows system. IMPORTANT: The target OS is Windows. Use Windows-compatible command-line syntax (e.g. use `echo. > filename` or `type nul > filename` to create empty files, do not use `touch`).


Example : 
User Query : What is the weather of new york?
Output : {{"step":"plan", "content":"The user is interested in weather data of new york"}}
Output : {{"step":"plan", "content":"From the available tools I should call get_weather tool for this "}}
Output : {{"step":"action", "function":"get_weather",
"input":"new york"
}}
Output : {{"step":"observe", "content":"26 degrees Celsius"}}
Output : {{"step":"final", "content":"The current weather of New York is 26 degrees Celsius"}}

"""


messages=[
   SystemMessage(content=system_prompt)
    
]


while True:
    query=input("> ")
    messages.append( HumanMessage(
        content=query
    ))

    while True:
        response=model.invoke(messages)
        parsed_response=json.loads(response.content)
        messages.append(AIMessage(content=json.dumps(   parsed_response)))


        if parsed_response.get("step") == "plan":
          print(f"AI : {parsed_response.get('content')}")
          continue



        if parsed_response.get("step") == "action":
            tool_name=parsed_response.get("function")
            tool_input=parsed_response.get("input")
            if tool_name in available_tools:
                tool=available_tools[tool_name]
                result=tool["fn"](tool_input)
                messages.append(AIMessage(content=f"Tool Output : {result}"))
                print(f"Observation : {result}")
                continue
            else:
                    messages.append(AIMessage(content=f"Error : Tool {tool_name} not found"))
                    print(f"Error : Tool {tool_name} not found")
                    continue
    
        if parsed_response.get("step") == "final":
                print(f"Final Answer : {parsed_response.get('content')}")
                break
    
    

    