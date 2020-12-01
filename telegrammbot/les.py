import requests
from bs4 import BeautifulSoup

url = 'https://binomo.com/trading'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)