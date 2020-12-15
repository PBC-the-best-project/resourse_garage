from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  # 升級的組合控制元件包
from tkinter.messagebox import showinfo, showwarning, showerror  # 各種型別的提示框
root = Tk()  # 初始化Tk()
root.title("hello tkinter")    # 設定視窗標題
root.geometry("800x1000")    # 設定視窗大小 注意：是x 不是*
root.resizable(width=True, height=True)  # 設定視窗是否可以變化長/寬，False不可變，True可變，預設為True
root.tk.eval('package require Tix')  # 引入升級包，這樣才能使用升級的組合控制元件
