import requests
from bs4 import BeautifulSoup
a = ""
url = 'https://zh.wikipedia.org/zh-tw/臺中高工'

response = requests.get(url)
if response.status_code == 200:
    page_content = response.text
    print(page_content)