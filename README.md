# AI-basics
its repo for revising the basics


# basic response from openai client will be like :
```
{
    "id": "chatcmpl-6v7mkQj980V1yBec6ETrKPRqFjNw9",
    "object": "chat.completion",
    "created": 1679001781,
    "model": "gpt-35-turbo",
    "usage": {
        "prompt_tokens": 95,
        "completion_tokens": 84,
        "total_tokens": 179
    },
    "choices": [
        {
            "message":
                {
                    "role": "assistant",
                    "content": "Yes, other Azure AI Services also support translation. Azure AI Services offer translation between multiple languages for text, documents, or custom translation through Azure AI Services Translator."
                },
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
```

# basic response from embedding model will be like
```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [
        0.0172990688066482523,
        -0.0291879814639389515,
        ....
        0.0134544348834753042,
      ],
      "index": 0
    }
  ],
  "model": "text-embedding-ada:002"
}
```


# Something about temperature and Top p
Adjusting model parameters
In addition to techniques discussed in this module, adjusting parameters of the model can have a significant impact on the response. In particular, temperature and top_p (top_probability) are the most likely to impact a model's response as they both control randomness in the model, but in different ways.

Higher values produce more creative and random responses, but will likely be less consistent or focused. Responses expected to be fictional or unique benefit from higher values for these parameters, whereas content desired to be more consistent and concrete should use lower values.

Try adjusting these parameters with the same prompt to see how they impact the response. It's recommended to change either temperature or top_p at a time, but not both.
refered from : https://learn.microsoft.com/en-us/training/modules/apply-prompt-engineering-azure-openai/2-understand-prompt-engineering


# Prompt Engineering Tips
1. ask clearly what exactly what you want, be as descriptive as possible
2. This method can be extrapolated to include complex instructions, such as a bulleted list of details to include, length of response, or desired formats to be included in the output. 
3. How instructions are formatted can impact how the model interprets the prompt. "*Recency bias*" can affect models, where information located towards the end of the prompt can have more influence on the output than information at the beginning. You may get better responses by repeating the instructions at the end of the prompt and assessing how that affects the generated response.
4. Use section markers :: A specific technique for formatting instructions is to split the instructions at the beginning or end of the prompt, and have the user content contained within --- or ### blocks. These tags allow the model to more clearly differentiate between instructions and content.
5. Primary content refers to content that is the subject of the query, such as a sentence to translate or an article to summarize. This content is often included at the beginning or end of the prompt (as an instruction and differentiated by --- blocks), with instructions explaining what to do with it.
6. Supporting content is content that may alter the response, but isn't the focus or subject of the prompt. Examples of supporting content include things like names, preferences, future date to include in the response, and so on. Providing supporting content allows the model to respond more completely, accurately, and be more likely to include the desired information.
7. Grounding content could be an essay or article that you then ask questions about, a company FAQ document, or information that is more recent than the data the model was trained on. If you need more reliable and current responses, or you need to reference unpublished or specific information, grounding content is highly recommended.
8. Specifying the structure of your output can have a large impact on your results.
ex. Put two fictional characters into JSON of the following format

{
  firstNameFictional: 
  jobFictional:
}

9. system message might include tone or personality, topics that shouldn't be included, or specifics (like formatting) of how to answer.
10. Asking a model to respond with the step by step process by which it determined the response is a helpful way to understand how the model is interpreting the prompt.
15. Cues are leading words for the model to build upon, and often help shape the response in the right direction.
ex. ```
Write a join query to get customer names with purchases in the past 30 days between tables named orders and customer on customer ID. 

SELECT
```
ex2. The model response picks up where the prompt left off, continuing in SQL, even though we never asked for a specific language. Other examples could be to help with python code, by giving code comments about the desired app and including import as a leading word at the end of the prompt, or similar in your desired language.
