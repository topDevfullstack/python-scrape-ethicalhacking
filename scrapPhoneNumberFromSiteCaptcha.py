from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse
import json
from bs4 import BeautifulSoup
import re

scrapfly = ScrapflyClient(key="Your API key")

def scrape_business(soup):
    company_name = soup.select_one("h1.dockable.business-name").text
    return company_name

def scrape_phone_numbers(soup):
    phone_number_pattern = r"[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\.\0-9]*(?=[^0-9])"
    all_text = soup.get_text()
    phone_numbers = []
    for phone_number in re.findall(phone_number_pattern, all_text):
        if len(phone_number.strip()) > 12:
            phone_numbers.append(phone_number)
    return phone_numbers

def scrape_pages(links: list):
    data = {}
    for link in links:
        api_response: ScrapeApiResponse = scrapfly.scrape(
            scrape_config=ScrapeConfig(
                url=link,
                # Activate the render_js feature to dynamic JavaScript content
                render_js=True,
                # Activate the anti scraping protection bypass to scrape without getting blocked
                asp=True,
                # Set the proxies location to the US to avoid Yellowpages regional blocking
                country="US",
            )
        )

        soup = BeautifulSoup(api_response.scrape_result["content"], "html.parser")
        company_name = scrape_business(soup)
        phone_numbers = scrape_phone_numbers(soup)
        if len(phone_numbers) > 0 and company_name not in data:
            data[company_name] = phone_numbers
    return data

data = scrape_pages(
    ["https://www.yellowpages.com/san-francisco-ca/mip/splunk-inc-4420913"]
)
# Print the result in JSON format
print(json.dumps(data, indent=4))
# {
#     "Splunk Inc": [
#         "(415) 848-8400",
#         "(415) 615-0396",
#         "(415) 568-4200",
#         "(415) 738-5456",
#         "(866) 438-7758",
#         "(888) 249-3263",
#         "(415) 848-8400"
#     ]
# }