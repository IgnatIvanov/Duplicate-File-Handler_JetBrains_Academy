import requests

from bs4 import BeautifulSoup

act = int(input())
url = str(input())

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a')
print(links[act - 1].get('href'))
