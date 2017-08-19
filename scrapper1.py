from bs4 import BeautifulSoup
from pip._vendor import requests

url = "http://www.skysports.com/football"

r = requests.get(url) #Retrieve URL

html = r.text #Return HTML as a string
soup = BeautifulSoup(html) #Convert to soup

print(soup.prettify()) #Output prettified version of soup
