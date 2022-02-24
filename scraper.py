import time
import re
import csv
# import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

address = "Marietta, GA 30067"
restaurant = "Taco Bell"

# try:
# restaurant = sys.argv[1]
# address = sys.argv[2]
# except:
# print("Unable to take cmd arguments.")

driver = webdriver.Chrome(executable_path=r'C:\Users\Owner\PycharmProjects\pythonScraper\chromedriver.exe')
driver.get("https://www.grubhub.com/")

driver.find_element(By.TAG_NAME, "input").send_keys(address)
driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(By.ID, "search-autocomplete-input").send_keys(restaurant)
driver.find_element(By.ID, "search-autocomplete-input").send_keys(Keys.ENTER)
time.sleep(2)

ht = driver.find_elements(By.TAG_NAME, 'span')
for elements in ht:
    values = elements.text
    break
if values.count(restaurant) >= 0:
    found = re.search('\\$(.+?) delivery', values).group()
    print(found)
else:
    print("The restaurant you're looking for isn't on GrubHub at this time.")
driver.close()

header = ['Address', 'Restaurant', 'Delivery Fee']
data = [address, restaurant, found]
with open('web-order.csv', 'w') as w:
    writer = csv.writer(w)
    writer.writerow(header)
    writer.writerow(data)
