import os
from winsound import Beep
import zipfile
import requests
from bs4 import BeautifulSoup
#import requests_html
import wget

# # for Grubhub - hardcoded to Marietta, Ga
# page = requests.get("https://bit.ly/3tEGNJM")
# soup = BeautifulSoup(page.content, 'html.parser')
# price_elements = soup.find_all("div", class_="u-text-secondary")
# # for elle in price_elements:
# #     print(elle, end="\n"*2)
# #session = requests_html.HTMLSession()

# # for DoorDash - hardcoded to Marietta, Ga
# page1 = requests.get("https://www.doordash.com/food-delivery/marietta-ga-restaurants/")
# soup1 = BeautifulSoup(page1.content, 'html.parser')
# price_elements1 = soup1.find_all("div", class_="sc-EHOje fZuZOJ")
# for elle in price_elements1:
#     print(elle, end="\n"*2)

# # placeholder
# page2 = ""

# print("Status code: " + str(page.status_code) + '\n')
# page.content


# #print(soup.prettify())

from selenium import webdriver
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text

# build the donwload url
download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

# download the zip file using the url built above
latest_driver_zip = wget.download(download_url,'chromedriver.zip')

# extract the zip file
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall() # you can specify the destination folder path here
# delete the zip file downloaded above
os.remove(latest_driver_zip)

driver = webdriver.Chrome(executable_path=r'C:\Users\Jairrel\Desktop\CS 4850\senior-proj\chromedriver.exe')
driver.get("https://bit.ly/3tEGNJM")

html1 = driver.page_source