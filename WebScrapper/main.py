import asyncio
from scraper import (
    all_paragraph_scraping,
    raw_data_scraping,
)
from crawler import crawl_web

input = ""

asyncio.run(raw_data_scraping(input))  
asyncio.run(all_paragraph_scraping(input)) 
 
#user inputs a query
#search engine starts to search through multiple websites to check
#for each website, put the link into input variable and scrape the relevant data
