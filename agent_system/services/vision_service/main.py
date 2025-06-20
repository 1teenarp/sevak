from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
from shared.ollama_client import call_ollama_with_image

app = FastAPI()

@app.post("/analyze")
async def analyze_image(
    file: UploadFile = File(...),
    prompt: str = Form("Describe this image")
):
    file_path = f"/data/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = await call_ollama_with_image(file_path, prompt)

    return JSONResponse(content={
        "filename": file.filename,
        "result": result
    })