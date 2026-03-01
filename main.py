# -*- coding: utf-8 -*-

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

system_prompt = os.getenv("SYSTEM_PROMPT")
API_KEY = os.getenv("API_KEY")
MODEL = "z-ai/glm-4.5-air:free"
MEMORY_FILE="memory.json"

MAX_MESSAGES=15

# -------------------------------
# 3️  Load / Save Memory
# -------------------------------

def load_memory(MEMORY_FILE):
    if not  os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE,"r",encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        print(f"❌ Failed to load memory: {str(e)}")
        return []

def save_memory(conversation):
    try:
        with open(MEMORY_FILE,"w",encoding="utf-8") as f:
            json.dump(conversation,f,indent=2,ensure_ascii=False)
    except Exception as e:
        print(f"❌ Failed to save memory: {str(e)}")

def clean_text(text):
    if not isinstance(text,str):
        text = str(text)
    replacements = {
        "–": "-",
        "—": "-",
        "→": "->",
        "“": '"',
        "”": '"',
        "’": "'",
#       "❤️": "",
#       "🔥": "",
#       "👋": ""
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text

conversation=[
{"role":"system","content":clean_text(system_prompt) }
]

cleaned_conversation = [
    {"role": msg["role"], "content": clean_text(msg["content"])}
    for msg in conversation
]

def send_to_model(conversation):
    try:
        response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages":conversation,
              },
        #verify=False
        timeout=30
    )

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            print(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        return (f"Error: {str(e)}")

#        Function call and Prompr input
def cli_loop():
    print("Welcome to VineAI❤️‍🔥\n")
    print("Chat started. Type exit to end chat.\n")
    while True:
        prompt = input("You: ")
        if prompt.lower()=="exit":
            print("Goodbye 👋")
            break
        conversation.append({"role":"user","content":clean_text(prompt)})
        answer=send_to_model(conversation)
        conversation.append({"role":"assistant","content":clean_text(answer)})
        if len(conversation) > MAX_MESSAGES:
            conversation[:]=[conversation[0]] + conversation[-(MAX_MESSAGES-1):]
        print("\nAnswer:")
        print(answer)

if __name__ == "__main__":
    cli_loop()
