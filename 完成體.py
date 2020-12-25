from __future__ import print_function
from PIL import Image,ImageTk
import tkinter as tk
from bs4 import BeautifulSoup
import requests
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# from bs4 import BeautifulSoup
import requests
import os

def variable():
    global name_variable,sex_variable, star_variable, city_variable, starnum
    name_variable = str(name_variable.get())
    sex_variable = str(sex_variable.get())
    star_variable = str(star_variable.get())
    city_variable = str(city_variable.get())
    starnum = star_dic.get(star_variable)

def google_photo(sex, season0, color0):
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_file.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=288, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])  # 所有圖片
    new_items = []  # 檔名＋ID
    if not items:
        print('No files found.')
    else:
        for item in items:
            new_items.append(u'{0}({1})'.format(item['name'][0:10], item['id']))
    photo = []  # 要找的照片的檔名+ID
    keyword_to_find = str(sex + season0 + '＿' + color0)  # 要找的照片的關鍵字:XX＿X，如：男秋＿白
    for a in new_items:
        if a.find(keyword_to_find) != -1:
            photo.append(a)
        else:
            continue
    # print(len(photo))  # 檢查是不是每個組合都是有照片的
    photo_path = os.getcwd()  # 這個py檔的路徑，因為載下來的照片會存在這個py檔旁邊
    pathlist = []
    for i in range(0, len(photo)):  # 4張圖片
        url = 'https://drive.google.com/u/0/uc?id=' + photo[i][11:-1] + '&export=download'
        photo_sourse = requests.get(url)  # 讀網址檔
        with open('image.' + 'test' + str(i) + '.png', 'wb') as file:
            file.write(photo_sourse.content)
            img_in_screen = Image.open(photo_path + '/image.test' + str(i) + '.png')
                # img_in_screen.show()
            # os.remove(path=path + '/image.test' + str(i) + '.png')  # 移除載下的圖片
            pathlist.append(photo_path + '/image.test' + str(i) + '.png')
    global path
    path = pathlist
    return path

def nextpage():
    name_frame.pack_forget()
    sex_frame.pack_forget()
    starsign_frame.pack_forget()
    next_btn.pack_forget()
    city_frame.pack_forget()
    global final_label, name_variable
    if sex_variable == '男':
        final_label.configure(text = name_variable[0] + "先生，這是您今天的最適穿著")
    else:
        final_label.configure(text=name_variable[0] + "小姐，這是您今天的最適穿著")

def luckystar():

    a = city_dic.get(city_variable)

    if a <= 9:
        url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX000' + \
               str(a) + ':1:TW?Goto=Redirected'
    elif a == 75:
        url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX0001:1:TW?Goto=Redirected'
    else:
        url2 = 'https://weather.com/zh-TW/weather/today/l/TWXX00' + \
               str(a) + ':1:TW?Goto=Redirected'
    r2 = requests.get(url2)

    c = starsign.index(star_variable) + 1
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
    common_use = str(num4[0].get_text()[index:]) + '：' + str(num3[0].get_text())
    if a == 1:
        string1 = str('彰化' + common_use)
    elif a == 2:
        string1 = str('嘉義' + common_use)
    elif a == 3:
        string1 = str('基隆' + common_use)
    elif a == 9:
        string1 = str('新竹' + common_use)
    elif a == 11:
        string1 = str('花蓮' + common_use)
    elif a == 13:
        string1 = str('高雄' + common_use)
    elif a == 14:
        string1 = str('苗栗' + common_use)
    elif a == 15:
        string1 = str('屏東' + common_use)
    elif a == 19:
        string1 = str('台中' + common_use)
    elif a == 20:
        string1 = str('台南' + common_use)
    elif a == 21:
        string1 = str('台北' + common_use)
    elif a == 22:
        string1 = str('新北' + common_use)
    elif a == 23:
        string1 = str('台東' + common_use)
    elif a == 25:
        string1 = str('桃園' + common_use)
    elif a == 42:
        string1 = str('金門' + common_use)
    elif a == 72:
        string1 = str('宜蘭' + common_use)
    elif a == 75:
        string1 = str('雲林' + common_use)
    elif a == 89:
        string1 = str('南投' + common_use)

    string2 = '溫度：'
    string2 += str(num2[0].get_text())
    string3 = str()

    for a in range(0, 3):
        string3 += num6[a].get_text() + '  ' + num5[a].get_text() + '\n'
    string3 += num6[3].get_text()
    # output
    now = datetime.datetime.now()  # 2019-04-11 14:18:41.629019
    otherStyleTime = now.strftime("%Y/%m/%d %H:%M:%S")  # 2019-04-11 14:18:41

    time_frame.grid(row=0, column=1, columnspan=2)
    time_label.configure(text=otherStyleTime + '   ' + string1 + '   ' + string2)
    time_label.grid()
    luck_frame.grid(row=1, column=1, columnspan=2)
    luck_label.configure(text=string3)
    luck_label.grid()

    temperature = int(string2[3:5])
    global season
    if temperature < 15:
        season = '冬'
    elif 15 <= temperature < 25:
        season = '秋'
    elif 25 <= temperature:
        season = '夏'

    global color
    color = lucky_color_dic.get(((int(otherStyleTime[5]) + int(otherStyleTime[6])) * int(otherStyleTime[8]) + int(otherStyleTime[9]) + starnum) % 12)

def photo():
    photo1_frame.grid(row=2, column=0)
    global photo1_label,photo1
    photo1 = Image.open(path[0])
    photo1 = photo1.resize(size)
    photo1 = ImageTk.PhotoImage(photo1)
    photo1_label.configure(image = photo1)
    photo1_label.grid()
    photo1_btn.grid()

    photo2_frame.grid(row=2, column=1)
    global photo2_label,photo2
    photo2 = Image.open(path[1])
    photo2 = photo2.resize(size)
    photo2 = ImageTk.PhotoImage(photo2)
    photo2_label.configure(image = photo2)
    photo2_label.grid()
    photo2_btn.grid()

    photo3_frame.grid(row=2, column=2)
    global photo3_label,photo3
    photo3 = Image.open(path[2])
    photo3= photo3.resize(size)
    photo3 = ImageTk.PhotoImage(photo3)
    photo3_label.configure(image = photo3)
    photo3_label.grid()
    photo3_btn.grid()

    photo4_frame.grid(row=2, column=3)
    global photo4_label,photo4
    photo4 = Image.open(path[3])
    photo4 = photo4.resize(size)
    photo4 = ImageTk.PhotoImage(photo4)
    photo4_label.configure(image = photo4)
    photo4_label.grid()
    photo4_btn.grid()

def variable_nextpage_luckystar_photo():
    variable()
    nextpage()
    luckystar()
    google_photo(sex_variable, season, color)
    photo()

def chose1():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    time_frame.grid_forget()
    luck_frame.grid_forget()
    global photo1
    final_label.pack(side = tk.TOP, padx=20, pady=10)
    final = tk.Label(window, image=photo1)
    final.pack(side=tk.TOP)
    for i in range(0,4):
        os.remove(path=path[i])

def chose2():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    time_frame.grid_forget()
    luck_frame.grid_forget()
    global photo2
    final_label.pack(side = tk.TOP, padx=20, pady=10)
    final = tk.Label(window, image=photo2)
    final.pack(side=tk.TOP)
    for i in range(0,4):
        os.remove(path=path[i])

def chose3():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    time_frame.grid_forget()
    luck_frame.grid_forget()
    global photo3
    final_label.pack(side = tk.TOP, padx=20, pady=10)
    final = tk.Label(window, image=photo3)
    final.pack(side=tk.TOP)
    for i in range(0,4):
        os.remove(path=path[i])

def chose4():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    time_frame.grid_forget()
    luck_frame.grid_forget()
    global photo4
    final_label.pack(side = tk.TOP, padx=20, pady=10)
    final = tk.Label(window, image=photo4)
    final.pack(side=tk.TOP)
    for i in range(0,4):
        os.remove(path=path[i])

window = tk.Tk()

window.title('星座穿搭')
window.geometry('1425x755')
window.configure(background='white')

path = []

name_variable = tk.StringVar()
name_frame = tk.Frame(window, bd=5)
name_frame.pack(side=tk.TOP, padx=20, pady=10)
name_label = tk.Label(name_frame, text='您的名字：')
name_label.pack(side=tk.LEFT)
name_entry = tk.Entry(name_frame, textvariable=name_variable)
name_entry.pack(side=tk.LEFT)

sex_frame = tk.Frame(window, bd=5)
sex_frame.pack(side=tk.TOP, padx=20, pady=10)
sex_label = tk.Label(sex_frame, text="性別：")
sex_label.pack(side=tk.LEFT)
sex_variable = tk.StringVar(window)
sex_variable.set('男')
sex_menu = tk.OptionMenu(sex_frame, sex_variable, *['男', '女'])
sex_menu.pack(side=tk.LEFT)

season = str()
starnum = int()
city_dic = {'彰化': 1, '嘉義': 2, '基隆': 3, '新竹': 9, '花蓮': 11, '高雄': 13, '苗栗': 14, '屏東': 15, '台中': 19, '台南': 20,
            '台北': 21, '新北': 22, '台東': 23, '桃園': 25, '金門': 42, '宜蘭': 72, '雲林': 75, '南投': 89}
star_dic = {'牡羊': 1, '金牛': 2, '雙子': 3, '巨蟹': 4, '獅子': 5,'處女': 6,
            '天秤': 7,'天蠍': 8,'人馬': 9,'魔羯': 10,'水瓶': 11,'雙魚': 0}
lucky_color_dic = {0: '藍', 1: '橘', 2: '綠', 3: '黑', 4: '黃', 5: '紅',
                   6: '紫', 7: '棕', 8: '杏', 9: '粉', 10: '灰', 11: '白'}
color = str()

star_variable = tk.StringVar(window)
star_variable.set('水瓶')
starsign = ['牡羊', '金牛', '雙子', '巨蟹', '獅子', '處女', '天秤', '天蠍', '人馬', '魔羯', '水瓶', '雙魚']
starsign_frame = tk.Frame(window, bd=5)
starsign_frame.pack(side=tk.TOP, padx=20, pady=10)
starsign_label = tk.Label(starsign_frame, text='星座：')
starsign_label.pack(side=tk.LEFT)
starsign_menu = tk.OptionMenu(starsign_frame, star_variable, *starsign)
starsign_menu.pack(side=tk.LEFT)

city_variable = tk.StringVar(window)
city_variable.set('基隆')
city = ['基隆','新北','台北','桃園','新竹','苗栗','台中','彰化','南投','雲林','嘉義','台南','高雄','屏東','宜蘭','花蓮','台東','金門']
city_frame = tk.Frame(window, bd=5)
city_frame.pack(side=tk.TOP, padx=20, pady=10)
city_label = tk.Label(city_frame, text='地點：')
city_label.pack(side=tk.LEFT)
city_menu = tk.OptionMenu(city_frame, city_variable, *city)
city_menu.pack(side=tk.LEFT)

next_btn = tk.Button(window, text='下一頁', command=variable_nextpage_luckystar_photo, bd=5)
next_btn.pack(side=tk.TOP, padx=20, pady=10)

time_frame = tk.Frame(window)
time_label = tk.Label(time_frame, text='')
luck_frame = tk.Frame(window)
luck_label = tk.Label(time_frame, text='')

photo1 = ImageTk
photo2 = ImageTk
photo3 = ImageTk
photo4 = ImageTk

size = (352,632)
photo1_frame = tk.Frame(window)
photo1_label = tk.Label(photo1_frame)
photo1_btn = tk.Button(photo1_frame, command=chose1, text='選擇', bd=5)

photo2_frame = tk.Frame(window)
photo2_label = tk.Label(photo2_frame)
photo2_btn = tk.Button(photo2_frame, command=chose2, text='選擇', bd=5)

photo3_frame = tk.Frame(window)
photo3_label = tk.Label(photo3_frame)
photo3_btn = tk.Button(photo3_frame, command=chose3, text='選擇', bd=5)

photo4_frame = tk.Frame(window)
photo4_label = tk.Label(photo4_frame)
photo4_btn = tk.Button(photo4_frame, command=chose4, text='選擇', bd=5)

final_frame = tk.Frame(window)
final_label = tk.Label(window)

window.mainloop()
