from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json
import time
# from config import ProductDetails, UserDetails, PaymentDetails, ChromeOptions

driver = webdriver.Chrome(executable_path='C:/Users/W 10/Desktop/chromedriver.exe')
wait = WebDriverWait(driver, 10)

driver.get('https://www.adidas.com/ng/ultraboost-5-dna-running-lifestyle-shoes/GV8745.html')

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="consent-tracking"]/div/div/div[3]/div/button[1]')))

affrim = driver.find_element_by_class_name("affirm")

if affrim:
    driver.find_element_by_class_name("affirm").click()

elems = driver.find_elements_by_class_name("size-radio")

active = []

for i in elems:
    attr = i.get_attribute("class").split(" ")
    if not "disabled\n" in attr:
        active.append(i)

active[0].click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-to-cart')))

button = driver.find_element_by_class_name("add-to-cart") 

print(button)

# button.click()


# driver.execute_script("arguments[0].click();", button)

# driver.find_element_by_class_name("minicart-total hide-no-link").click()


