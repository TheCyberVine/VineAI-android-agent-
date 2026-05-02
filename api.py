import requests
from config import MODEL,API_KEY

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
            "messages": conversation,
              },
        #verify=False
        timeout=30
    )

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            print(f"Error {response.status_code}: {response}")

    except Exception as e:
        return (f"Error: {str(e)}")
