from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
from tools import Tools, FUNCTION_NAME_TO_FUNCTION_MAP
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

messages.append({
    "role":"system",
    "content":"give the answer in the such a curious way. For example When the user ask about "
    "the set in cpp Answer why set is required and how can it will be useful and short examples and ask questions. give the answer within 150 words donot make to much long"
})


# looping Start for the tool: 
while True:
    user_input=input("\n You:")

    if user_input.lower() in ["exit","quit","bye","goodbye"]:
        break

    messages.append({
        "role":"user",
        "content":user_input,
    })


    response=client.chat.completions.create(
    model=os.getenv("MODEL", "qwen3:4b"),
    messages=messages,
    tools=Tools,
    )

    msg=response.choices[0].message
    if msg.tool_calls:
        messages.append(msg)

        for tool_call in msg.tool_calls:
            func_name=tool_call.function.name
            func_arg=json.loads(tool_call.function.arguments or "{}")  # convert the json into dictionary 

            fn=FUNCTION_NAME_TO_FUNCTION_MAP[func_name]
            result=fn(**func_arg)

        messages.append({
            "role":"tool",
            "tool_id":"tool_call.id",
            "content":str(result)

        })

        # second call to llm api 
        response=client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )

        msg=response.choices[0].message

    messages.append({
        "role":"assistant",
        "content":"msg.content"
    })

    print("Assistant  "+ msg.content)


