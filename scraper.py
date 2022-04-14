import time
import re
import csv
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

address = "Marietta, GA 30067"
restaurant = "Burger King"
values = ""
temp1 = address
temp2 = restaurant
try:
    address = sys.argv[1]
    restaurant = sys.argv[2]
except:
    print("Unable to take cmd arguments.")
#print(restaurant)
#print(address)
#print(temp1 == address)
#print(temp2 == restaurant)
#linux imports
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("https://www.grubhub.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
driver.find_element(By.TAG_NAME, "input").send_keys(address)
driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-autocomplete-input")))
driver.find_element(By.ID, "search-autocomplete-input").send_keys(restaurant)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-autocomplete-input")))
driver.find_element(By.ID, "search-autocomplete-input").send_keys(Keys.ENTER)

time.sleep(2)
site1 = driver.find_elements(By.TAG_NAME, 'div')
for elements in site1:
    values = elements.text
    #print(values)
    break
if values.count(restaurant) >= 0:
    try:
        found1 = re.search('\\$(.+?) delivery', values).group()
    except:
        found1 = "Unavailable"
    #print(found1)
else:
    found1 = "The restaurant you're looking for isn't on GrubHub at this time."

driver.get("https://www.ubereats.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "location-typeahead-home-input")))
driver.find_element(By.ID, "location-typeahead-home-input").send_keys(address)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "location-typeahead-home-menu")))
driver.find_element(By.ID, "location-typeahead-home-input").send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(restaurant)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(Keys.ENTER)

time.sleep(2.5)
site2 = driver.find_elements(By.TAG_NAME, 'div')
for elements in site2:
    values = elements.text
    #print(values)
    break
if values.count(restaurant) >= 0:
    try:
        found2 = re.search('\\$(.+?) Delivery Fee', values).group()
    except:
        found2 = "Unavailable"

    #print(found2)
else:
    found2 ="The restaurant you're looking for isn't on UberEats at this time."

driver.get("https://www.postmates.com/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
driver.find_element(By.TAG_NAME, "input").send_keys(address)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "location-typeahead-home-menu")))
driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(restaurant)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(Keys.ENTER)
time.sleep(2.5)
site3 = driver.find_elements(By.TAG_NAME, 'div')
for elements in site3:
    values = elements.text
    #print(values)
    break
if values.count(restaurant) >= 0:
    try:
        found3 = re.search('\\$(.+?) Delivery Fee', values).group()
    except:
        found3 = "Unavailable"
    #print(found3)
else:
    found3 = "The restaurant you're looking for isn't on Postmates at this time."

driver.close()
print("Grubhub")
print(found1)
print("Uber Eats")
print(found2)
print("Postmates")
print(found3)
#header = ['Delivery Site', 'Restaurant', 'Delivery Fee']
#data1 = ["Grubhub", restaurant, found1]
#data2 = ["Ubereats", restaurant, found2]
#data3 = ["Postmates", restaurant, found3]
#with open('web-order.csv', 'w') as w:
#    writer = csv.writer(w)
#    writer.writerow(header)
#    writer.writerow(data1)
#    writer.writerow(data2)
#    writer.writerow(data3)
