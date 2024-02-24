from dotenv import load_dotenv
import os
import openai
import requests

# Load environment variables from config.env
load_dotenv('secrets.env')

# Access your API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Function to analyze user input and extract interests and risk preference
def analyze_user_input(text):
    openai.api_key = openai_api_key
    
    # Analyze text for interests and risk preference
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following user input for interests and stock preferences, and estimate their risk aversion: {text}",
        max_tokens=1024
    )
    
    interests = response.choices[0].text.split('\n')[0]  # Simplified extraction
    risk_aversion = response.choices[0].text.split('\n')[1]  # Simplified extraction
    return interests, risk_aversion

# Function to fetch stocks based on interests
def fetch_stocks_based_on_interests(interests):
    # Placeholder for fetching stocks based on interests
    # This could be an API call to a financial data provider
    # For demonstration, we return a static list of stocks
    return ["AAPL", "TSLA", "GOOGL", "AMZN", "MSFT", "FB", "NFLX", "NVDA", "INTC", "AMD"]

# Main function to generate stock recommendations and risk aversion coefficient
def generate_stock_recommendations(user_input):
    interests, risk_aversion = analyze_user_input(user_input)
    
    # Fetch stocks based on analyzed interests
    recommended_stocks = fetch_stocks_based_on_interests(interests)
    
    return recommended_stocks, risk_aversion

# Example usage
user_input = "I'm interested in technology and renewable energy. I prefer investments with moderate risk."
recommended_stocks, risk_aversion = generate_stock_recommendations(user_input)
print("Recommended Stocks:", recommended_stocks)
print("Risk Aversion:", risk_aversion)