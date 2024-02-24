from dotenv import load_dotenv
import os
import openai

# Load environment variables from config.env
load_dotenv('secrets.env')

# Replace "your_api_key_here" with your actual OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_stock_list(prompt):
    response = openai.Completion.create(
        model="text-davinci-004", # You can change this to "gpt-4" when it's officially supported in the API
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n", "and", ",", ".", ";"]
    )
    # Assuming the API returns a comma-separated list of stock symbols or names
    stock_list = response.choices[0].text.strip().split(', ')
    # Return at most 10 stocks
    return stock_list[:10]

# Example prompt
prompt = "Generate a list of at most 10 promising tech stocks for investment in 2024."

# Get the list of stocks
stock_list = get_stock_list(prompt)
print(stock_list)
