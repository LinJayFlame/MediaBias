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
        "num_results": 2  # Number of results you want
    }
    
    response = requests.post(BASE_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns the search results as JSON
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

company = "BBC News"
query = f"""
    You are a useful search engine for {company}.
    The user wants to search for articles about the negative effects of technology or AI on learning or education 

Rules:
1. Provide only the correct unique URLs for {company} that talks about the impact of technology on education
2. Do not show the intermediate steps
"""

# Example Usage
# results = query_perplexity(query)


# "https://www.bbc.com/news/business-34174795",
# "https://www.bbc.com/news/business-34671952",
# "https://www.brookings.edu/articles/ai-and-the-next-digital-divide-in-education",
# "https://www.brookings.edu/articles/the-world-needs-a-premortem-on-generative-ai-and-its-use-in-education",
# "https://www.channelnewsasia.com/today/voices/commentary-cyberloafing-new-norm-among-youths-why-its-bad-and-how-tackle-it-4867506",
# "https://www.channelnewsasia.com/singapore/commentary-real-culprit-making-our-children-dumb-isnt-e-learning-990926",

results = [
"https://www.forbes.com/sites/michaelhorn/2017/11/14/new-research-answers-whether-technology-is-good-or-bad-for-learning",
"https://www.forbes.com/sites/ronschmelzer/2024/05/28/how-ai-is-shaping-the-future-of-education"
]



for i in range(len(results)):
    asyncio.run(all_paragraph_scraping(results[i], i))








#gives a sentiment analysis on each company based on a given topic
#when user queries
#perplexity AI queries based on that query and the news sources that we saved in our database
#for each of the news (maybe we query 5 related news for each source) in each of the news source , 
# we implement all paragraph scraping and run Keith's backeng logic on the scraped text to give it a setimental score.)
#the aggregation of the sentimental scores reflect the overall sentimental score of that news source on that topic


#user inputs a query
#search engine starts to search through multiple websites to check
#for each website, put the link into input variable and scrape the relevant data
