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
        "query": query,
        "num_results": 5
    }
    
    response = requests.post(BASE_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

agencyList = ["BBC News", "Brookings", "CNA", "CNN", "Forbes", "The Guardian", "The Straits Times"]

results = []
for agency in agencyList:
    query = f"""
        You are a useful search engine for {agency}.
        The user wants to search for articles about the negative effects of technology or AI on learning or education 

    Rules:
    1. Provide only the correct unique URLs for {agency} that talks about the impact of technology on education
    2. Do not show the intermediate steps
    """
    results.append(query_perplexity(query))

# Example Processed Results List:
results = [
"https://www.channelnewsasia.com/commentary/tech-solutions-problems-smart-city-user-design-4788581",
"https://www.channelnewsasia.com/commentary/ai-potential-reshape-societies-industries-healthcare-climate-change-4951701"
"https://www.bbc.com/news/business-34174795",
"https://www.bbc.com/news/business-34671952",
"https://www.brookings.edu/articles/ai-and-the-next-digital-divide-in-education",
"https://www.brookings.edu/articles/the-world-needs-a-premortem-on-generative-ai-and-its-use-in-education",
"https://www.channelnewsasia.com/today/voices/commentary-cyberloafing-new-norm-among-youths-why-its-bad-and-how-tackle-it-4867506",
"https://www.channelnewsasia.com/singapore/commentary-real-culprit-making-our-children-dumb-isnt-e-learning-990926",
"https://www.forbes.com/sites/michaelhorn/2017/11/14/new-research-answers-whether-technology-is-good-or-bad-for-learning",
"https://www.forbes.com/sites/ronschmelzer/2024/05/28/how-ai-is-shaping-the-future-of-education",
"https://www.bbc.com/storyworks/specials/the-new-normal/the-drive-to-do-good"
]

for i in range(len(results)):
    asyncio.run(all_paragraph_scraping(results[i], i))
