from bs4 import BeautifulSoup
import requests
import datetime
a = int(input())  # 地點

url1 = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6300400'
r1 = requests.get(url1)
if a <= 9:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX000' + \
        str(a) + ':1:TW?Goto=Redirected'
else:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX00' + \
        str(a) + ':1:TW?Goto=Redirected'
# https://weather.com/zh-TW/weather/today/l/ab6a0d440cf29997c96b86e11b647c285d3a489a623ea04d29fdefe0ea3534b2
# https://weather.com/zh-TW/weather/today/l/7ceb69e37a100e138b92e592f2bd6619cfa4626f7315d0877b5061494e83bb77
# https://weather.com/zh-TW/weather/today/l/fe7393b7f2c8eed2cf692bd079361df362d9f0c1c0f896e6e46a649295e15c7d
r2 = requests.get(url2)

soup1 = BeautifulSoup(r1.text, 'html.parser')
soup2 = BeautifulSoup(r2.text, 'html.parser')

list1 = []
num1 = soup1.find_all('li', class_="ttem-C")  # 溫度
list1.append(num1[0].get_text()+'：')
attr1 = {'class': 'CurrentConditions--tempValue--3KcTQ'}
num2 = soup2.find_all('span', attrs=attr1)  # 溫度值
attr2 = {'class': 'CurrentConditions--phraseValue--2xXSr'}
num3 = soup2.find_all('div', attrs=attr2)  # 天氣
attr3 = {'class': 'CurrentConditions--location--1Ayv3'}
num4 = soup2.find_all('h1', attrs=attr3)  # 地點

for value in num2:
    list1.append(value.get_text())  # 溫度＋溫度值

string1 = str(num4[0].get_text()) + '：' + str(num3[0].get_text())
string2 = str()
for a in range(len(list1)):
    string2 += list1[a]

# output
now = datetime.datetime.now()  # 2019-04-11 14:18:41.629019
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")  # 2019-04-11 14:18:41
print(otherStyleTime)

print(string1)  # 地點 & 天氣

information = string2.split('：')
temperature = int(information[1][:-1])
print(temperature)  # 當下溫度數值
