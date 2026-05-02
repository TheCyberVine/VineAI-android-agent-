import json
import os
from config import MEMORY_FILE

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load memory: {str(e)}")
        return []

def save_memory(conversation):
    try:
        with open(MEMORY_FILE,"w",encoding="utf-8") as f:
            json.dump(conversation,f,indent=2,ensure_ascii=False)
    except Exception as e:
        print(f"❌ Failed to save memory: {str(e)}")
