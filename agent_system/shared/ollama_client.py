# Interface to communicate with Ollama server
# from dotenv import load_dotenv
import os
import httpx
import requests

# load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://192.168.1.119:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:latest")

OLLAMA_URL = OLLAMA_HOST+"/api/generate"

def query_ollama(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]


async def call_ollama_with_image(image_path: str, prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [image_path]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{OLLAMA_HOST}/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response")
