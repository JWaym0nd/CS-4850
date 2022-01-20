import requests
from bs4 import BeautifulSoup

# for Grubhub - hardcoded to Marietta, Ga
page = requests.get("https://bit.ly/3tEGNJM")

# for DoorDash - hardcoded to Marietta, Ga
page1 = requests.get("https://www.doordash.com/food-delivery/marietta-ga-restaurants/")

# placeholder
page2 = ""

print("Status code: " + str(page.status_code) + '\n')
page.content

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())