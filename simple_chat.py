from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
from tools import Tools, FUNCTION_NAME_TO_FUNCTION_MAP
from utils.utility import debugTool
from tools import runTool
import json 


# Load the project settings from the .env file beside this script.
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)


# Ollama does not validate this key, but the OpenAI Python client requires
# a non-empty api_key when it is created.
client = OpenAI(
    base_url=os.getenv("BASE_URL", "http://127.0.0.1:11434/v1"),
    api_key=os.getenv("API_KEY") or "ollama",
)

messages=[]
# Assignnign the Role to Model How to acts and behave 
maxStep=5

messages.append({
    "role":"system",
    "content":"give the answer in the such a curious way. For example When the user ask about "
    "the set in cpp Answer why set is required and how can it will be useful and short examples and ask questions. give the answer within 150 words donot make to much long"
})


# Chat Loops Start from Here  
while True:
    user_input=input("\n You:")

    if user_input.lower() in ["exit","quit","bye","goodbye"]:
        break

    messages.append({
        "role":"user",
        "content":user_input,
    })

# Chain Looping Start from Here 

    # while True: - To prevent from infinite tool calling we are moving to for loop
    for loop in range(maxStep):
        # Tools Calling Garna 
            response=client.chat.completions.create(
            model=os.getenv("MODEL", "qwen3:4b"),
            messages=messages,
            tools=Tools
            )

            msg=response.choices[0].message # message append form the tools calls 

            if not msg.tool_calls:      # If not find any tools just break from the loop
                 break  

            debugTool(f"Step {maxStep+1} : model requrest len{msg.tool_calls}")
            

            messages.append(msg)        # Just append the msg in the messages until we get

            for tool_call in msg.tool_calls: # tool call and execute 
                result=runTool(tool_call)
               



            debugTool(f"    {result}")
            messages.append({
            "role":"tool",
            "tool_id":"tool_call.id",
            "content":str(result)
            })
        
    messages.append({
         "role":"assistant",
         "content":"msg.content"
    })
    print("Assistant  "+(msg.content or "" ))


