# core/agent.py
import requests

OLLAMA_URL = "http://192.168.1.119:11434/api/generate"
MODEL_NAME = "gemma3:latest"

def query_ollama(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]

if __name__ == "__main__":
    print(query_ollama(str(input())))