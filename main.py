from config import system_prompt,MAX_MESSAGES
from api import send_to_model
from memory import save_memory,load_memory
from router import handle_command

# -*- coding: utf-8 -*-


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

conversation=load_memory()
if not conversation:
    conversation=[
{"role":"system","content":clean_text(system_prompt) }
]

"""cleaned_conversation = [
    {"role": msg["role"], "content": clean_text(msg["content"])}
    for msg in conversation
]"""


#        Function call and Prompr input
def cli_loop():
    print("Welcome to VineAI❤️‍🔥\n")
    print("Chat started. Type exit to end chat.\n")
    while True:
        prompt = input("You: ")

        if prompt.lower()=="exit":
            save_memory(conversation)
            print("Goodbye 👋")
            break
        if handle_command(prompt,conversation):
            continue

        conversation.append({"role":"user","content":clean_text(prompt)})
        answer=send_to_model(conversation)
        conversation.append({"role":"assistant","content":clean_text(answer)})
        if len(conversation) > MAX_MESSAGES:
            conversation[:]=[conversation[0]] + conversation[-(MAX_MESSAGES-1):]
        print("\nAnswer:")
        print(answer)

if __name__ == "__main__":
    cli_loop()
