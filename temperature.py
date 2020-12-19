import requests
url1 = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6300400'
r1 = requests.get(url1)
url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW?Goto=Redirected'
r2 = requests.get(url2)
# print(r.text)
from bs4 import BeautifulSoup
soup1 = BeautifulSoup(r1.text, 'html.parser')
soup2 = BeautifulSoup(r2.text, 'html.parser')

list1 = []
num1 = soup1.find_all('li', class_="ttem-C")
list1.append(num1[0].get_text()+'：')
attr1 = {'class': 'CurrentConditions--tempValue--3KcTQ'}
num2 = soup2.find_all('span', attrs=attr1)
attr2 = {'class': 'CurrentConditions--phraseValue--2xXSr'}
num3 = soup2.find_all('div', attrs=attr2)
attr3 = {'class': 'CurrentConditions--location--1Ayv3'}
num4 = soup2.find_all('h1', attrs=attr3)

for value in num2:
    list1.append(value.get_text())

string1 = str(num4[0].get_text()) + '：' + str(num3[0].get_text())
string2 = str()
for a in range(len(list1)):
    string2 += list1[a]
print(string1)
print(string2)

