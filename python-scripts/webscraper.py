import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time 

# Download chrom driver from https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/
browser = webdriver.Chrome(executable_path = '') # TODO update file path to wherever you put the chromedriver locally
browser.get('') # TODO add the url for the website you'll be scraping
delay = 25 # wait 25s to let the website load

try:
    # Sample code of logging into a website
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, "input-62"))) 
    email = browser.find_element(By.ID, "input-62")
    email.send_keys('name@email.com', Keys.TAB)
    password = browser.find_element(By.ID, "input-65")
    password.send_keys('PASSWORD', Keys.TAB + Keys.TAB + Keys.ENTER)
except TimeoutException:
    print ("Loading took too much time")

# Adding sleeps between sures data is loaded
# Sampele code of how to find different elements
time.sleep(5)
browser.find_element(By.ID, "search").send_keys(Keys.TAB + Keys.TAB + Keys.ENTER + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
time.sleep(5)
browser.find_element(By.XPATH, '//span[text()="EXPORT DATA"]').click()
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="app"]/div[4]/div/div/div[2]/div/button[2]/span/div').click()
time.sleep(5)