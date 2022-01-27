from winsound import Beep
import requests
from bs4 import BeautifulSoup
#import requests_html

# for Grubhub - hardcoded to Marietta, Ga
page = requests.get("https://bit.ly/3tEGNJM")
soup = BeautifulSoup(page.content, 'html.parser')
price_elements = soup.find_all("div", class_="u-text-secondary")
# for elle in price_elements:
#     print(elle, end="\n"*2)
#session = requests_html.HTMLSession()

# for DoorDash - hardcoded to Marietta, Ga
page1 = requests.get("https://www.doordash.com/food-delivery/marietta-ga-restaurants/")
soup1 = BeautifulSoup(page1.content, 'html.parser')
price_elements1 = soup1.find_all("div", class_="sc-EHOje fZuZOJ")
for elle in price_elements1:
    print(elle, end="\n"*2)

# placeholder
page2 = ""

print("Status code: " + str(page.status_code) + '\n')
page.content


#print(soup.prettify())