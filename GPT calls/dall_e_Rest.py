from openai import AzureOpenAI
import json
api_base = ''  # Enter your endpoint here
api_key = ''        # Enter your API key here
# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint=api_base,
    api_key=api_key
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="robotic theam with black background and cloudlex written on it",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)