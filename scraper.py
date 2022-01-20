import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.doordash.com/food-delivery/marietta-ga-restaurants/")
page
print("Status code: " + str(page.status_code) + '\n')
page.content

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())