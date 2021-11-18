import requests
from bs4 import BeautifulSoup

URL = 'https://gamestatus.info/far-cry-6?lg=en'

reqs = requests.get(URL)

soup = BeautifulSoup(reqs.text, 'lxml')
print(soup.prettify())
