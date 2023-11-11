from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Open the 2048 game website using Selenium
driver = webdriver.Chrome()
driver.get("https://play2048.co/")
time.sleep(3)
while True:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)
    time.sleep(0.1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_LEFT)
    time.sleep(0.1)
    
