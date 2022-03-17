import time
import re
import csv
# import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

address = "Marietta, GA 30067"
restaurant = "Burger King"
values = ""

# try:
# restaurant = sys.argv[1]
# address = sys.argv[2]
# except:
# print("Unable to take cmd arguments.")

driver = webdriver.Chrome(executable_path=r'C:\Users\johnr\PycharmProjects\pythonProject\chromedriver.exe')

driver.get("https://www.grubhub.com/")
driver.find_element(By.TAG_NAME, "input").send_keys(address)
time.sleep(1)
driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.ID, "search-autocomplete-input").send_keys(restaurant)
driver.find_element(By.ID, "search-autocomplete-input").send_keys(Keys.ENTER)
time.sleep(1)

site1 = driver.find_elements(By.TAG_NAME, 'div')
time.sleep(2)
for elements in site1:
    values = elements.text
    break
if values.count(restaurant) >= 0:
    found1 = re.search('\\$(.+?) delivery', values).group(0)
    print(found1)
else:
    print("The restaurant you're looking for isn't on GrubHub at this time.")

driver.get("https://www.ubereats.com/")
driver.find_element(By.ID, "location-typeahead-home-input").send_keys(address)
time.sleep(1)
driver.find_element(By.ID, "location-typeahead-home-input").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(restaurant)
driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(Keys.ENTER)
time.sleep(1)

site2 = driver.find_elements(By.TAG_NAME, 'div')
time.sleep(2)
for elements in site2:
    values = elements.text
    break
if values.count(restaurant) >= 0:
    found2 = re.search('\\$(.+?) Delivery Fee', values).group(0)
    print(found2)
else:
    print("The restaurant you're looking for isn't on UberEats at this time.")

driver.get("https://www.postmates.com/")
driver.find_element(By.TAG_NAME, "input").send_keys(address)
time.sleep(2)
driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(restaurant)
driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(Keys.ENTER)
time.sleep(1)

site3 = driver.find_elements(By.TAG_NAME, 'div')
time.sleep(2)
for elements in site3:
    values = elements.text
    break
if values.count(restaurant) >= 0:
    found3 = re.search('\\$(.+?) Delivery Fee', values).group(0)
    print(found3)
else:
    print("The restaurant you're looking for isn't on Postmates at this time.")

driver.close()

header = ['Address', 'Restaurant', 'Delivery Fee']
data1 = [address, restaurant, found1]
data2 = [address, restaurant, found2]
data3 = [address, restaurant, found3]
with open('web-order.csv', 'w') as w:
    writer = csv.writer(w)
    writer.writerow(header)
    writer.writerow(data1)
    writer.writerow(data2)
    writer.writerow(data3)
