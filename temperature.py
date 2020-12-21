from bs4 import BeautifulSoup
import requests
import datetime
a = int(input())  # 地點
b = int(input('請輸入：1~4 (1今日運勢/2明日運勢/3本週運勢/4本月運勢) '))  # 1今日/2明日/3本週/4本月
c = int(input('請輸入：1~12 (1牡羊/2金牛/3雙子/4巨蟹/5獅子/6處女/7天秤/8天蠍/9射手/10摩羯/11水瓶/12雙魚) '))
# c星座：1牡羊/2金牛/3雙子/4巨蟹/5獅子/6處女/7天秤/8天蠍/9射手/10摩羯/11水瓶/12雙魚

url1 = 'https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6300400'
r1 = requests.get(url1)

if a <= 9:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX000' + \
        str(a) + ':1:TW?Goto=Redirected'
else:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX00' + \
        str(a) + ':1:TW?Goto=Redirected'
r2 = requests.get(url2)

url3 = 'http://tw.xingbar.com/cgi-bin/v5starfate2?fate=' + str(b) + '&type=' + str(c)
r3 = requests.get(url3)

soup1 = BeautifulSoup(r1.text, 'html.parser')
soup2 = BeautifulSoup(r2.text, 'html.parser')
soup3 = BeautifulSoup(r3.text, 'html.parser')

list1 = []
num1 = soup1.find_all('li', class_="ttem-C")  # 溫度
list1.append(num1[0].get_text()+'：')
attr1 = {'class': 'CurrentConditions--tempValue--3KcTQ'}
num2 = soup2.find_all('span', attrs=attr1)  # 溫度值
attr2 = {'class': 'CurrentConditions--phraseValue--2xXSr'}
num3 = soup2.find_all('div', attrs=attr2)  # 天氣
attr3 = {'class': 'CurrentConditions--location--1Ayv3'}
num4 = soup2.find_all('h1', attrs=attr3)  # 地點
attr4 = {'class': 'dotRbox dottxt'}
num5 = soup3.find_all('div', attrs=attr4)  # 愛情＋工作＋幸運色＋幸運物
attr5 = {'class': 'dotLbox dottxt'}
num6 = soup3.find_all('div', attrs=attr5)  # 心情＋財運＋健康＋開運方位

for value in num2:
    list1.append(value.get_text())  # 溫度＋溫度值

string1 = str(num4[0].get_text()) + '：' + str(num3[0].get_text())
string2 = str()
string3 = str()

for a in range(len(list1)):
    string2 += list1[a]

for a in range(len(num5)):
    string3 += num6[a].get_text() + '  ' + num5[a].get_text() + '\n'
# output
now = datetime.datetime.now()  # 2019-04-11 14:18:41.629019
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")  # 2019-04-11 14:18:41
print(otherStyleTime)

print(string1)  # 地點 & 天氣
print(string2)  # 溫度
print(string3)  # 星座運

temperature = int(list1[1][:-1])  # 比較用
print(temperature)  # 當下溫度數值
