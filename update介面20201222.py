# -*- coding: utf8 -*-
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import StringVar
# import cairosvg                 # for svg (need install)
# import io                       # for svg (already with python file)
from PIL import ImageTk, Image    # for png (need install)
import csv
import tkinter.messagebox
from tkinter import Frame

csv_file = 0                      # 要選哪一個csv檔(區域)
food_type = 0
staple_food = 0
budget = 0

class FoodSelector(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self, background = '#E4C4A7')
        self.grid()
        start()
        # self.configure(background = '#E4C4A7')  # 視窗底色 ECDCC2
        # self.change() 
        
class start(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self, background = '#E4C4A7')
        self.grid()
        self.start_window()
        # self.configure(background = '#E4C4A7')  # 視窗底色 ECDCC2


    def start_window(self):
        # window = tk.Toplevel()
        # window.grid()
        # window.geometry('500x300')
        # self.configure(background = '#E4C4A7')
        f2 = tkFont.Font(size = 48, family = "微軟正黑體")
        
        self.start_lbltitle = tk.Label(self, text = "今天吃什麼?", height = 1, width = 12, font = f2, fg = "#996F4C", bg = "#F6ECE4")
        self.start_lbltitle.grid(row = 0, column = 0, rowspan = 1, columnspan = 4, sticky = tk.W+tk.E+tk.S+tk.N)
        
        self.start_button = tk.Button(self, text = "get start", height = 3, width = 15, font = f2, command = self.change, bd = 0, bg = '#E4C4A7')
        self.start_button.grid(row = 1, column = 1, rowspan = 1, columnspan = 1)
        # return window
        
    def change(self):       
        self.destroy()
        map_window()  # self.master
        
class choose(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self, height = 100, width = 1000, background = '#E4C4A7')
        self.grid()
        self.create_window()
        # self.start_window()
        # self.configure(background = '#E4C4A7')  # 視窗底色 ECDCC2
    
    def create_window(self):     # 條件選擇頁面
        # window = tk.Toplevel()
        # window.grid()
        # window.geometry('500x300')
        f1 = tkFont.Font(size = 12, family = "標楷體")
        
        dict1 = {"中式":["米食", "麵類", "餃類", "鍋類"], "日式":["拉麵", "米食"], "韓式":["ALL"], "南洋":["ALL"], "美式":["速食", "牛排", "其他"], "義式":["ALL"], "印式":["ALL"], "其他":["ALL"]}
        var_material = tk.StringVar()

        
        self.label1 = tk.Label(self, text = "想吃什麼風格的食物", height = 3, width = 15, font = f1, fg = "Blue")
        self.label1.grid(row = 0, column = 3, sticky = tk.W+tk.E) 
        

        self.combobox1 = ttk.Combobox(self, values = list(dict1.keys()), textvariable=var_material, state="readonly")
        self.combobox1.bind('<<ComboboxSelected>>', lambda event: self.combobox2.config(values=dict1[var_material.get()]))  # 第二個下拉選單隨第一個變動
        self.combobox1.grid(row = 1, column = 3, sticky = tk.W+tk.E)
        
        self.label2 = tk.Label(self, text = "想吃什麼主食", height = 3, width = 15, font = f1, fg = "Blue")
        self.label2.grid(row = 3, column = 3, sticky = tk.W+tk.E) 
        
        self.combobox2 = ttk.Combobox(self, state="readonly")
        self.combobox2.grid(row = 4, column = 3, sticky = tk.W+tk.E)
        
        self.label3 = tk.Label(self, text = "想花多少錢", height = 3, width = 15, font = f1, fg = "Blue")
        self.label3.grid(row = 6, column = 3, sticky = tk.W+tk.E) 
        
        self.combobox3 = ttk.Combobox(self, values = ["100以下", "100-200", "200-350", "350以上"], state="readonly")
        self.combobox3.grid(row = 7, column = 3, sticky = tk.W+tk.E)
 
        self.button_sure = tk.Button(self, text = "確認", height = 2, width = 15, font = f1, fg = "Red", command = lambda:[self.checkcmb_1(), self.checkcmb_2(), self.checkcmb_3(), self.change()])
        self.button_sure.grid(row = 15, column = 3, sticky = tk.W+tk.E)
    
    # 紀錄每個下拉選單選擇的值
    def checkcmb_1(self):
        global food_type
        
        if self.combobox1.get() == "中式":
            food_type = "C"
        elif self.combobox1.get() == "日式":
            food_type = "J"
        elif self.combobox1.get() == "韓式":
            food_type = "K"
        elif self.combobox1.get() == "南洋":
            food_type = "S"
        elif self.combobox1.get() == "美式":
            food_type = "A"
        elif self.combobox1.get() == "義式":
            food_type = "I"
        elif self.combobox1.get() == "印式":
            food_type = "IN"
        elif self.combobox1.get() == "其他":
            food_type = "O"
            
    def checkcmb_2(self):
        global staple_food
        
        if self.combobox2.get() == "米食":
            staple_food = "R"
        elif self.combobox2.get() == "麵類" or "拉麵":
            staple_food = "N"
        elif self.combobox2.get() == "餃類":
            staple_food = "D"
        elif self.combobox2.get() == "鍋類":
            staple_food = "P"
        elif self.combobox2.get() == "ALL":
            staple_food = ""
        elif self.combobox2.get() == "速食":
            staple_food = "F"
        elif self.combobox2.get() == "牛排":
            staple_food = "S"
        elif self.combobox2.get() == "其他":
            staple_food = "O"
    
    def checkcmb_3(self):
        global budget
        
        if self.combobox3.get() == "100以下":
            budget = "100"
        elif self.combobox3.get() == "100-200":
            budget = "200"
        elif self.combobox3.get() == "200-350":
            budget = "300"
        elif self.combobox3.get() == "350以":
            budget = "350"
    
    def change(self):
        self.destroy()
        result()
        
class map_window(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self, background = '#E4C4A7', height = 800, width = 800)
        # self.geometry('800x800')
        self.grid()
        self.createWidgets()

 
    def createWidgets(self):     # 起始頁面
        
        f1 = tkFont.Font(size = 48, family = "微軟正黑體")
        
    
        load_1 = Image.open("台大校區測試2.png")
        self.image_1 = ImageTk.PhotoImage(load_1)
        self.button_map_1 = tk.Button(self, image = self.image_1, height = 500, width = 500, command = lambda:[self.change(), self.choose_csv1()], bd = 0)
        self.button_map_1.grid(row = 2, column = 1, rowspan = 4 , columnspan = 3, sticky = tk.N)
        
        load_2 = Image.open("公館測試2.png")
        self.image_2 = ImageTk.PhotoImage(load_2)
        self.button_map_2 = tk.Button(self, image = self.image_2, height = 300, width = 300, command = lambda:[self.change(), self.choose_csv2()], bd = 0)
        self.button_map_2.grid(row = 3, column = 0, rowspan = 3 , columnspan = 1)

        load_3 = Image.open("溫州街測試2.png")
        self.image_3 = ImageTk.PhotoImage(load_3)
        self.button_map_3 = tk.Button(self, image = self.image_3, height = 300, width = 200, command = lambda:[self.change(), self.choose_csv3()], bd = 0)
        self.button_map_3.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, sticky = tk.E)


        load_4 = Image.open("118測試2.png")
        self.image_4 = ImageTk.PhotoImage(load_4)
        self.button_map_4 = tk.Button(self, image = self.image_4, height = 100, width = 200, command = lambda:[self.change(), self.choose_csv4()], bd = 0)
        self.button_map_4.grid(row = 1, column = 3, rowspan = 1 , columnspan = 1, sticky = tk.E)

        
    def change(self):
        self.destroy()
        choose()  # self.master
        
    def choose_csv1(self):   # 根據使用者點擊不同區域，選擇不同csv檔
        global csv_file
        csv_file = "校內.csv"
    
    def choose_csv2(self):
        global csv_file
        csv_file = "公館.csv"
        
    def choose_csv3(self):
        global csv_file
        csv_file = "溫州街.csv"
        
    def choose_csv4(self):
        global csv_file
        csv_file = "118.csv"


class result(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_window()

    def create_window(self):
         
        f1 = tkFont.Font(size = 24, family = "標楷體")
        f2 = tkFont.Font(size = 24, family = "微軟正黑體")
        selected_rst = []     # 最後要呈現的所有店家
        
        with open(csv_file, "r", newline='', encoding = "utf8") as csvfile:
            cheader = csvfile.readline()
            reader = csv.DictReader(csvfile, fieldnames=("店家名稱", "風格", "主食", "價位"), quotechar='"')
            for arow in reader:
                if food_type in arow["風格"] and staple_food in arow["主食"] and budget in arow["價位"]:
                    selected_rst.append(arow["店家名稱"])
        
        if selected_rst == []:       # 沒有符合條件的餐廳
            self.label_nomatch1 = tk.Label(self, text = "OOOPS 沒有符合的餐廳", height = 3, width = 50, font = f1, fg = "Red")
            self.label_nomatch1.grid(row = 3, column = 3, sticky = tk.W+tk.E) 
            self.label_nomatch2 = tk.Label(self, text = "再試試別的搜尋條件吧", height = 3, width = 50, font = f1, fg = "Red")
            self.label_nomatch2.grid(row = 4, column = 3, sticky = tk.W+tk.E)
            self.button_return= tk.Button(self, text="返回", height = 3, width = 10, font = f2, fg = "Black", command = self.change)
            self.button_return.grid(row = 6, column = 3, rowspan = 1 , columnspan = 1, sticky = tk.W+tk.E)
            
        else:                        # 顯示餐廳
            self.Lb1 = tk.Label(self, text = "以下餐廳推薦給您:)", height = 10, width = 50, font = f1, fg = "Blue")
            self.Lb1.pack() 
            self.rst_lbl = tk.Listbox(self)
            
            for i in range(len(selected_rst)):
                self.rst_lbl.insert(i, selected_rst[i])
                self.rst_lbl.itemconfig(i, foreground="purple")
                self.rst_lbl.pack()
            
            self.button_return= tk.Button(self, text="再一次", height = 1, width = 10, font = f2, fg = "Black", command = self.change)
            self.button_return.pack()
            self.button_return= tk.Button(self, text="結束", height = 1, width = 10, font = f2, fg = "Black", command = self.quit)
            self.button_return.pack()
        
    def change(self):
        self.destroy()
        start()
            
        


my_selector = FoodSelector()
my_selector.master.title("My selector")
my_selector.mainloop()
