from bs4 import BeautifulSoup
from pip._vendor import requests

url = "http://www.skysports.com/football"

r = requests.get(url)

html = r.text
soup = BeautifulSoup(html)

print(soup.prettify())
