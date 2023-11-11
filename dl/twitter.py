from selenium import webdriver
import urllib.request
import time
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://twitter.com/cat_auras")

time.sleep(3)

for i in range(3):
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)

time.sleep(3)

images = driver.find_elements(By.TAG_NAME, 'img')
for i, image in enumerate(images):
    print("正在下載第" + str(i) + "張圖片")
    src = image.get_attribute('src')
    response = requests.get(src, stream=True)
    if response.status_code == 200:
        with open(f'image{i}.png', 'wb') as out_file:
            out_file.write(response.content)