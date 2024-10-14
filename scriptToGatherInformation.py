import requests
from bs4 import BeautifulSoup

url = 'https://themes.muffingroup.com/be/hotel6/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract WordPress version
meta_generator = soup.find('meta', {'name': 'generator'})
if meta_generator:
    print(f"WordPress Version: {meta_generator['content']}")

# Extract installed plugins (if visible)
plugins = []
for link in soup.find_all('link'):
    if 'wp-content/plugins' in link.get('href', ''):
        plugin = link['href'].split('/')[5]
        plugins.append(plugin)
print(f"Installed Plugins: {set(plugins)}")
