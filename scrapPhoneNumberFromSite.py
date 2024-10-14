from playwright.sync_api import sync_playwright
import httpx
from bs4 import BeautifulSoup
import re
import json

# Scrape links function we created earlier
def scrape_yellowpages_search(url):
    with sync_playwright() as playwight:
        browser = playwight.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page_content = page.content()
        soup = BeautifulSoup(page_content, "html.parser")
        links = []
        for link_box in soup.select("div.info-section.info-primary"):
            link = "https://www.yellowpages.com" + link_box.select_one("a").attrs["href"]
            links.append(link)
    return links

def scrape_phone_numbers(links: list):
    # Empty object to save the data into
    data = {}
    for link in links:
        page_response = httpx.get(url=link)
        # Get a BeautifulSoup for each page HTML
        soup = BeautifulSoup(page_response.text, "html.parser")
        # Scrape the company name
        company_name = parse_business(soup)
        # Scrape phone numbers in the HTML
        phone_numbers = parse_phone_numbers(soup)
        # Check if we go phone numbers and company name doesn't exist in the data object
        if len(phone_numbers) > 0 and company_name not in data:
            data[company_name] = phone_numbers
    return data


def parse_business(soup):
    company_name = soup.select_one("h1.dockable.business-name").text
    return company_name

def parse_phone_numbers(soup):
    # Regex pattern used to search for numbers
    phone_number_pattern = r"[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.\0-9]*(?=[^0-9])"
    # Get all text in the HTML page
    all_text = soup.get_text()
    phone_numbers = []
    # Loop through all phone numbers found the text
    for phone_number in re.findall(phone_number_pattern, all_text):
        # Check if this is a valid phone number by checking the length 
        if len(phone_number.strip()) > 12:
            phone_numbers.append(phone_number)
    return phone_numbers

# Get all page links in the main search page
links = scrape_yellowpages_search("https://www.yellowpages.com/search?search_terms=software+company&geo_location_terms=San+Francisco%2C+CA")
# Scrape phone numbers data from all links
data = scrape_phone_numbers(links)

# Print the result in JSON format
print(json.dumps(data, indent=4))