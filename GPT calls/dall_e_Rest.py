import requests
import time
import os
api_base = '<your_endpoint>'  # Enter your endpoint here
api_key = '<your_key>'        # Enter your API key here

api_version = '2024-02-01'
url = f"{api_base}/openai/deployments/<dalle3>/images/generations?api-version={api_version}"
headers= { "api-key": api_key, "Content-Type": "application/json" }
body = {
    # Enter your prompt text here
    "prompt": "A multi-colored umbrella on the beach, disposable camera",
    "size": "1024x1024", # supported values are “1792x1024”, “1024x1024” and “1024x1792” 
    "n": 1, #The number of images to generate. Only n=1 is supported for DALL-E 3.
    "quality": "hd", # Options are “hd” and “standard”; defaults to standard 
    "style": "vivid" # Options are “natural” and “vivid”; defaults to “vivid”
}
submission = requests.post(url, headers=headers, json=body)

image_url = submission.json()['data'][0]['url']

print(image_url)