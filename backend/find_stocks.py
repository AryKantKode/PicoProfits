from dotenv import load_dotenv
import os
import openai
from openai import OpenAI

# Load environment variables from the .env file
load_dotenv('secrets.env')

# Function to fetch stock list based on the prompt
def stock_list(prompt):
    #Initialize client
    client = OpenAI()

    # Ensure the API key is loaded from environment variables
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    # Create a completion request to GPT-4
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Generate a space-separated string of at most 10 stock symbols based on the following prompt: " + prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Return the text of the response
    return response.choices

# Example usage:
prompt = "I'm interested in technology and renewable energy sectors."
print(stock_list(prompt))