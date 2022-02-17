import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\johnr\PycharmProjects\pythonProject\chromedriver.exe')
driver.get("https://www.grubhub.com/")
address = "Marietta, GA 30067"
driver.find_element(By.TAG_NAME, "input").send_keys(address)
driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)
time.sleep(1)
restaurant = "Burger King"
driver.find_element(By.ID, "search-autocomplete-input").send_keys(restaurant)
driver.find_element(By.ID, "search-autocomplete-input").send_keys(Keys.ENTER)
time.sleep(1)

ht = driver.find_elements(By.TAG_NAME, 'span')
for elements in ht:
    values = elements.text
    break
if values.count(restaurant) >= 3:
    found = re.search('\\$(.+?) delivery', values).group()
    print(found)
else:
    print("The restaurant you're looking for isn't on GrubHub at this time.")
driver.close()
