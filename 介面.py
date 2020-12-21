from PIL import Image

import tkinter as tk
import time


def nextpage():
    name_frame.pack_forget()
    sex_frame.pack_forget()
    starsign_frame.pack_forget()
    next_btn.pack_forget()
    city_frame.pack_forget()
    photo1_frame.grid(row = 0, column = 0)
    photo1_label.grid()
    photo1_btn.grid()
    photo2_frame.grid(row = 0, column = 1)
    photo2_label.grid()
    photo2_btn.grid()
    photo3_frame.grid(row = 0, column = 2)
    photo3_label.grid()
    photo3_btn.grid()
    photo4_frame.grid(row = 0, column = 3)
    photo4_label.grid()
    photo4_btn.grid()

def chose1():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    final = tk.Label(window, image = photo1)
    final.pack(side = tk.TOP)
def chose2():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    final = tk.Label(window, image = photo2)
    final.pack(side = tk.TOP)
def chose3():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    final = tk.Label(window, image = photo3)
    final.pack(side = tk.TOP)
def chose4():
    photo1_frame.grid_forget()
    photo2_frame.grid_forget()
    photo3_frame.grid_forget()
    photo4_frame.grid_forget()
    final = tk.Label(window, image = photo4)
    final.pack(side = tk.TOP)



window = tk.Tk()

window.title('星座穿搭')
window.geometry('1500x1000')
window.configure(background='white')

name = tk.StringVar()
name_frame = tk.Frame(window, bd = 5)
name_frame.pack(side = tk.TOP, padx=20, pady=10)
name_label = tk.Label(name_frame, text = '您的名字')
name_label.pack(side = tk.LEFT)
name_entry = tk.Entry(name_frame, textvariable=name)
name_entry.pack(side = tk.LEFT)

sex_frame = tk.Frame(window, bd = 5)
sex_frame.pack(side = tk.TOP, padx=20, pady=10)
sex_label = tk.Label(sex_frame, text = "性別")
sex_label.pack(side = tk.LEFT)
sex_variable = tk.StringVar(window)
sex_variable.set('男')
sex_menu = tk.OptionMenu(sex_frame, sex_variable, *['男', '女'])
sex_menu.pack(side = tk.LEFT)

date = time.strftime("%m/%d", time.localtime())

star_variable = tk.StringVar(window)
star_variable.set('水瓶')
starsign = ['水瓶','雙魚','牡羊','金牛','雙子','巨蟹','獅子','處女','天秤','天蠍','人馬','魔羯']
starsign_frame = tk.Frame(window, bd = 5)
starsign_frame.pack(side = tk.TOP, padx=20, pady=10)
starsign_label = tk.Label(starsign_frame, text = '星座')
starsign_label.pack(side = tk.LEFT)
starsign_menu = tk.OptionMenu(starsign_frame, star_variable, *starsign)
starsign_menu.pack(side = tk.LEFT)

city = tk.StringVar()
city_frame = tk.Frame(window, bd = 5)
city_frame.pack(side = tk.TOP, padx=20, pady=10)
city_label = tk.Label(city_frame, text = '城市')
city_label.pack(side = tk.LEFT)
city_entry = tk.Entry(city_frame, textvariable=city)
city_entry.pack(side = tk.LEFT)

next_btn = tk.Button(window, text = '下一頁', command = nextpage, bd = 5)
next_btn.pack(side = tk.TOP, padx=20, pady=10)
'''
photo1_frame = tk.Frame(window)
photo1 = Image.open('C:/Daniel/報告/日系簡約風＿春秋＿白色.png')
photo1 = photo1.resize((photo1.width // 2, photo1.height // 2))
photo1_label = tk.Label(photo1_frame ,image=photo1)
photo1_btn = tk.Button(photo1_frame, command = chose1, text = '選擇', bd = 5)

photo2_frame = tk.Frame(window)
photo2 = tk.PhotoImage('photo2', file='C:/Daniel/報告/日系簡約風＿夏＿綠色.png')
photo2_label = tk.Label(photo2_frame ,image=photo2)
photo2_btn = tk.Button(photo2_frame, command = chose2, text = '選擇', bd = 5)

photo3_frame = tk.Frame(window)
photo3 = tk.PhotoImage('photo3', file='C:/Daniel/報告/型男工裝風＿夏＿灰色.png')
photo3_label = tk.Label(photo3_frame ,image=photo3)
photo3_btn = tk.Button(photo3_frame, command = chose3, text = '選擇', bd = 5)

photo4_frame = tk.Frame(window)
photo4 = tk.PhotoImage('photo4', file='C:/Daniel/報告/韓系男友風＿冬＿白色.png')
photo4_label = tk.Label(photo4_frame ,image=photo4)
photo4_btn = tk.Button(photo4_frame, command = chose4, text = '選擇', bd = 5)
'''
window.mainloop()