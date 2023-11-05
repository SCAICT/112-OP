import requests
from bs4 import BeautifulSoup
x = input("請輸入維基百科網址:")
url = 'https://zh.m.wikipedia.org/zh-tw/' + x
response = requests.get(url)
if response.status_code == 200:
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html5lib')

    wiki = soup.find_all('p')[0].get_text()
    if wiki.replace("\n", "").strip() == '':
        wiki = soup.find_all('p')[1].get_text()
    print(wiki)