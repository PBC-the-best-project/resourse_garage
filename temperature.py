import requests
url = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6300400'
r = requests.get(url)
# print(r.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

num1 = soup.find_all('li', class_="ttem-C")
for info in num1:
    print(info.get_text())
    print('-----')

