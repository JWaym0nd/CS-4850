import os
from winsound import Beep
import zipfile
from matplotlib.pyplot import text
import requests
from bs4 import BeautifulSoup
import wget
import time

# #print(soup.prettify())

from selenium import webdriver
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text

if os.path.exists('chromedriver.exe'):    
    try:    
        os.remove('chromedriver.exe')
    except:
        print("Couldn't remmove old Chromedriver")

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
soup = BeautifulSoup(driver.page_source, 'html.parser')
price_elements = soup.find_all(class_="u-text-secondary")
for elle in price_elements:
    print(elle, end="\n"*2)

#ht = driver.find_elements_by_class_name("u-text-secondary") 
ht = driver.find_elements_by_tag_name("div")
#ht = driver.find_elements_by_link_text("$3.49 delivery")
#ht = driver.find_elements_by_id("text-delivery-fee")
#ht = driver.find_element_by_css_selector("delivery-fee-info")

time.sleep(1)

for elements in ht:
    try:
        print(elements.text)
    except:
        print("Can't get.")
        


# for element in ht:
#     if (element.text != "Asian" or element.text != "GreeK" or element.text != "American" or element.text
#     != "Indian" or element.text != "Dessert" or element.text != "Mexican" or element.text != "Chicken"
#     or "Curry"):
#         ht.pop(ht.index(element))

driver.close()