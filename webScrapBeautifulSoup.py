# Web Scraping with BeautifulSoup
import requests
from bs4 import BeautifulSoup
url = "https://www.genfluence.ai"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h2")
print("Latest Headlines:")
for headline in headlines:
    print(headline.text)