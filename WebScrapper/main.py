import os
import asyncio
import requests
from dotenv import load_dotenv
from scraper import (
    all_paragraph_scraping,
    raw_data_scraping,
)
load_dotenv()

API_KEY = os.getenv('API_KEY')

# Replace with your actual Perplexity API key
BASE_URL = "https://api.perplexity.ai/search"

def query_perplexity(query):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "query": query,  # Your search query
        "num_results": 5  # Number of results you want
    }
    
    response = requests.post(BASE_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns the search results as JSON
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

#getting user enquiry
input = ""

# asyncio.run(raw_data_scraping(input))  
asyncio.run(all_paragraph_scraping(input)) 


# Example Usage
results = query_perplexity("")
print(results)

 
#gives a sentiment analysis on each company based on a given topic
#when user queries
#perplexity AI queries based on that query and the news sources that we saved in our database
#for each of the news (maybe we query 5 related news for each source) in each of the news source , 
# we implement all paragraph scraping and run Keith's backeng logic on the scraped text to give it a setimental score.)
#the aggregation of the sentimental scores reflect the overall sentimental score of that news source on that topic


#user inputs a query
#search engine starts to search through multiple websites to check
#for each website, put the link into input variable and scrape the relevant data
