import tkinter as tk
import random as r
import time
from datetime import datetime

class KapchaApp():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Пытаемся в капчи")
        self.window.geometry("500x500")
        self.window.focus_set()
        self.create_widgets()
        self.capcha.focus_set()
        self.len = 5 ###длина капчи
        self.window.bind('n',self.create_capcha)
        self.capcha.bind('<Return>',self.valid_capch)

    def create_widgets(self):
        self.label = tk.Label(text="Место для лучшей капчи",bg="yellow", fg="black",font="Courier 20",width=38, height=5)
        self.capcha = tk.Text(bg="white", fg="black",font="Courier 14",width=20, height=5)
        self.label.pack()


    def create_capcha(self,event):
        self.capcha.delete(0.0, tk.END)
        self.s = str()  ###авто капчи
        for i in range(self.len):
            self.s += str(r.randint(0, 9))
        self.label['text'] = self.s
        self.capcha.pack()
        self.start =  datetime.now()

    def valid_capch(self,event):
        self.cur_capch = self.capcha.get(0.0,tk.END).replace('\n', '')
        self.capcha.delete(0.0,tk.END)
        self.end = (datetime.now() - self.start)
        if self.s == self.cur_capch:
            self.label['text'] = "Успех"+' '+ str(self.end)# '%M,%S',
        else:
            print(self.cur_capch)

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    KapchaApp().start()