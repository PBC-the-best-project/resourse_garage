from bs4 import BeautifulSoup
import requests
import datetime
from PIL import Image
while True:
    try:
        c = int(input('請輸入：1~12 (1牡羊/2金牛/3雙子/4巨蟹/5獅子/6處女/7天秤/8天蠍/9射手/10摩羯/11水瓶/12雙魚) '))
        # c星座：1牡羊/2金牛/3雙子/4巨蟹/5獅子/6處女/7天秤/8天蠍/9射手/10摩羯/11水瓶/12雙魚
        if not 1 <= c <= 12:
            print('超出範圍！')
            continue
        else:
            break
    except ValueError:
        print('請輸入數字')
a = int()
if a <= 9:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX000' + \
        str(a) + ':1:TW?Goto=Redirected'
elif a == 75:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX0001:1:TW?Goto=Redirected'
else:
    url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX00' + \
        str(a) + ':1:TW?Goto=Redirected'
r2 = requests.get(url2)

url3 = 'http://tw.xingbar.com/cgi-bin/v5starfate2?fate=1&type=' + str(c)
r3 = requests.get(url3)

soup2 = BeautifulSoup(r2.text, 'html.parser')
soup3 = BeautifulSoup(r3.text, 'html.parser')

attr1 = {'class': 'CurrentConditions--tempValue--3KcTQ'}
num2 = soup2.find_all('span', attrs=attr1)  # 溫度值
attr2 = {'class': 'CurrentConditions--phraseValue--2xXSr'}
num3 = soup2.find_all('div', attrs=attr2)  # 天氣
attr3 = {'class': 'CurrentConditions--location--1Ayv3'}
num4 = soup2.find_all('h1', attrs=attr3)  # 地點
attr4 = {'class': 'dotRbox dottxt'}
num5 = soup3.find_all('div', attrs=attr4)  # 愛情＋工作21＋幸運物
num5.remove(num5[2])
attr5 = {'class': 'dotLbox dottxt'}
num6 = soup3.find_all('div', attrs=attr5)  # 心情＋財運＋健康＋開運方位

index = num4[0].get_text().find(' 天氣')
'''
1彰化/2嘉義/3基隆/9新竹/11花蓮/13高雄/14苗栗/15屏東/19台中/20台南/21台北/
22新北/23台東/25桃園/42金門/72宜蘭/75雲林/89南投
'''
if a == 1:
    string1 = str('彰化' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 2:
    string1 = str('嘉義' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 3:
    string1 = str('基隆' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 9:
    string1 = str('新竹' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 11:
    string1 = str('花蓮' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 13:
    string1 = str('高雄' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 14:
    string1 = str('苗栗' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 15:
    string1 = str('屏東' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 19:
    string1 = str('台中' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 20:
    string1 = str('台南' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 21:
    string1 = str('台北' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 22:
    string1 = str('新北' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 23:
    string1 = str('台東' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 25:
    string1 = str('桃園' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 42:
    string1 = str('金門' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 72:
    string1 = str('宜蘭' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 75:
    string1 = str('雲林' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
elif a == 89:
    string1 = str('南投' + num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())

string2 = '溫度：'
string3 = str()
string2 += str(num2[0].get_text())

for a in range(0, 3):
    string3 += num6[a].get_text() + '  ' + num5[a].get_text() + '\n'
string3 += num6[3].get_text()
# output
now = datetime.datetime.now()  # 2019-04-11 14:18:41.629019
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")  # 2019-04-11 14:18:41
print(otherStyleTime)

print(string1)  # 地點 & 天氣
print(string2)  # 溫度
print(string3)  # 星座運

temperature = int(num2[0].get_text()[0:-1])  # 比較用
print(temperature)  # 當下溫度數值

'''
3Chi-Lung/11Hualian/19Taichung Tw-Afb/21Taipei Songshan Airport/
22New Taipei City/23Taidong/42Chin-Men/72I-Lan/89Nan-Tou
'''