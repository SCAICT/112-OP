import requests
from bs4 import BeautifulSoup
x = input("想要查甚麼: ")
url = 'https://zh.m.wikipedia.org/zh-tw/' + x
response = requests.get(url).text
soup = BeautifulSoup(response, 'html5lib')
wiki = soup.find_all('p')[0].get_text()
if wiki.replace("\n", "").strip() == '':
    wiki = soup.find_all('p')[1].get_text()
print(wiki)