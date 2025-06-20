# Interface to communicate with Ollama server
import os
import httpx

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

async def call_ollama_with_image(image_path: str, prompt: str, model: str = "llava:latest"):
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [image_path]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{OLLAMA_HOST}/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response")
