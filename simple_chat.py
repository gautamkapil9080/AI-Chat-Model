from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

# The .env file is in the AI Assistant folder, next to this script's folder.
env_path = Path(__file__).parent / "AI Assistant" / ".env"
load_dotenv(env_path)

# Ollama does not validate this key, but the OpenAI Python client requires
# a non-empty api_key when it is created.
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY") or "ollama",
)
messages=[]


while True:
    user_input=input("\n You:")

    if user_input.lower() in ["exit","quit","bye","goodbye"]:
        break

    messages.append({
        "role":"user",
        "content":user_input
    })

    response=client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=messages
    )
    
    messages.append({
        "role":"assitant",
        "content":"response.choices[0].message.content"
    })

    print("AIBHAI",response.choices[0].message.content)


