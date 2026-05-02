import os
from dotenv import load_dotenv

load_dotenv()

system_prompt = os.getenv("SYSTEM_PROMPT")
API_KEY = os.getenv("API_KEY")
#MODEL = "z-ai/glm-4.5-air:free"
#MODEL = "stepfun/step-3.5-flash:free"
#MODEL = "google/gemma-4-26b-a4b-it:free"
#MODEL = "google/gemma-4-31b-it:free"
MODEL = "openrouter/owl-alpha"
MEMORY_FILE="memory.json"

MAX_MESSAGES=15
