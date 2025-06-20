# Entry point for agent logic (e.g., CLI or daemon)
import requests
import os

def run_vision_inference(image_path: str, prompt: str):
    url = "http://localhost:8002/analyze"
    with open(image_path, "rb") as f:
        files = {"file": (os.path.basename(image_path), f, "image/jpeg")}
        data = {"prompt": prompt}
        response = requests.post(url, files=files, data=data)
    result = response.json()
    print("\n--- Vision Inference Result ---")
    print(f"File: {result.get('filename')}")
    print(f"Response: {result.get('result')}")

def main():
    print("Agent is starting up...")
    # Demo call
    test_image = "./data/sample.jpg"  # Ensure this exists
    test_prompt = "What is shown in this image?"
    if os.path.exists(test_image):
        run_vision_inference(test_image, test_prompt)
    else:
        print(f"Test image not found: {test_image}")

if __name__ == "__main__":
    main()