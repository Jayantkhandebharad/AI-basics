#step1 :
# Add OpenAI library
from openai import AzureOpenAI

deployment_name = '<YOUR_DEPLOYMENT_NAME>' 

# step 2: Initialize the Azure OpenAI client
client = AzureOpenAI(
        azure_endpoint = '<YOUR_ENDPOINT_NAME>', 
        api_key='<YOUR_API_KEY>',  
        api_version="20xx-xx-xx" #  Target version of the API, such as 2024-02-15-preview
        )

# step 3: call to gpt and remember the model name is given while call
response = client.chat.completions.create(
    model=deployment_name, #it is used while calling
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]
)

# you can check I have written basic response structure in .md file
generated_text = response.choices[0].message.content

# Print the response
print("Response: " + generated_text + "\n")