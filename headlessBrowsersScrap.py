from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_yellowpages_search(url):
    # Intitialize a playwright instance
    with sync_playwright() as playwight:
        # Launch a chrome headless browser
        browser = playwight.chromium.launch(headless=True)
        # Create a new page inside the browser
        page = browser.new_page()
        # Go to the page URL
        page.goto(url)
        # Get the page HTML content
        page_content = page.content()
        # Create a BeautifulSoup object
        soup = BeautifulSoup(page_content, "html.parser")
        links = []
        # Loop through all result boxes in the search result
        for link_box in soup.select("div.info-section.info-primary"):
            # Extract the page link
            link = "https://www.yellowpages.com" + link_box.select_one("a").attrs["href"]
            links.append(link)
    return links

links = scrape_yellowpages_search("https://www.yellowpages.com/search?search_terms=software+company&geo_location_terms=San+Francisco%2C+CA")
print(links)