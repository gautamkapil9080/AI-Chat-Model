from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

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
while True:
    user_input=input("\n You:")

    if user_input.lower() in ["exit","quit","bye","goodbye"]:
        break

    messages.append({
        "role":"user",
        "content":user_input
    })

    response=client.chat.completions.create(
    model=os.getenv("MODEL", "qwen3:4b"),
    messages=messages
    )
    
    messages.append({
        "role":"assistant",
        "content":response.choices[0].message.content
    })

    print("AIBHAI",response.choices[0].message.content)


