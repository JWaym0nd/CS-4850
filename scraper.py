import time
import re
import multiprocessing
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


address = "Marietta, GA 30067"
restaurant = "Burger King"
try:
    address = sys.argv[1]
    restaurant = sys.argv[2]
except:
    print("Unable to take cmd arguments.")


def grub_hub():
    global address
    global restaurant
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.grubhub.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    driver.find_element(By.TAG_NAME, "input").send_keys(address)
    driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-autocomplete-input")))
    driver.find_element(By.ID, "search-autocomplete-input").send_keys(restaurant)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-autocomplete-input")))
    driver.find_element(By.ID, "search-autocomplete-input").send_keys(Keys.ENTER)

    time.sleep(3)
    site1 = driver.find_elements(By.TAG_NAME, 'div')
    for elements in site1:
        values = elements.text
        break
    if values.count(restaurant) >= 0:
        try:
            found = re.search('\\$(.+?) delivery', values).group()
        except:
            found = "Unavailable"
    else:
        found = "The restaurant you're looking for isn't on GrubHub at this time."
    driver.close()
    print("Grubhub")
    print(found)


def uber_eats():
    global address
    global restaurant
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.ubereats.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "location-typeahead-home-input")))
    driver.find_element(By.ID, "location-typeahead-home-input").send_keys(address)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "location-typeahead-home-menu")))
    driver.find_element(By.ID, "location-typeahead-home-input").send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
    driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(restaurant)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
    driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(Keys.ENTER)

    time.sleep(3)
    site2 = driver.find_elements(By.TAG_NAME, 'div')
    for elements in site2:
        values = elements.text
        break
    if values.count(restaurant) >= 0:
        try:
            found = re.search('\\$(.+?) Delivery Fee', values).group()
        except:
            found = "Unavailable"
    else:
        found = "The restaurant you're looking for isn't on UberEats at this time."
    driver.close()
    print("Uber Eats")
    print(found)


def post_mates():
    global address
    global restaurant
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.postmates.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    driver.find_element(By.TAG_NAME, "input").send_keys(address)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "location-typeahead-home-menu")))
    driver.find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
    driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(restaurant)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
    driver.find_element(By.ID, "search-suggestions-typeahead-input").send_keys(Keys.ENTER)
    time.sleep(3)
    site3 = driver.find_elements(By.TAG_NAME, 'div')
    for elements in site3:
        values = elements.text
        break
    if values.count(restaurant) >= 0:
        try:
            found = re.search('\\$(.+?) Delivery Fee', values).group()
        except:
            found = "Unavailable"
    else:
        found = "The restaurant you're looking for isn't on Postmates at this time."
    driver.close()
    print("Postmates")
    print(found)


def main():
    p1 = multiprocessing.Process(target=grub_hub)
    p2 = multiprocessing.Process(target=uber_eats)
    p3 = multiprocessing.Process(target=post_mates)

    # Start each thread
    p1.start()
    p2.start()
    p3.start()

    # Wait until each thread finishes
    p1.join()
    p2.join()
    p3.join()


if __name__ == "__main__":
    main()
