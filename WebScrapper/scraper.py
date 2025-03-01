import requests
from bs4 import BeautifulSoup

async def scrape(url):
    try:
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html5lib")
        return request, soup
    except Exception as e:
        print(e)
        return None, None

async def raw_data_scraping(query):
    try:
        request, soup = await scrape(query)
        file_write = open(f"RawData.txt", "w")
        file_write.write(f"{request.content}")
        file_write.close()
        return
    except Exception as e:
        return e

async def all_paragraph_scraping(query, i):
    try:
        request, soup = await scrape(query)
        file_write = open(f"scraped{i}.txt", "w")
        paragraph = ""
        for para in soup.find_all("p"):
            paragraph = para.get_text()
            file_write.write(f"{paragraph}\n\n")
        file_write.close()
    except Exception as e:
        return e