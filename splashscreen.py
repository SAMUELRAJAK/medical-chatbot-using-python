from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql

from tkinter.ttk import Progressbar
import tkinter.ttk as ttk


splashscreen = Tk()

splashscreen.geometry('500x500+510+200')
splashscreen.resizable(0, 0)
bgImage=tk.PhotoImage(file='images/splashscreen.png')
bgLabel=Label(splashscreen,image=bgImage)
splashscreen.overrideredirect(True)
bgLabel.place(x=0,y=0)


"""
def mainwindow():
    splashscreen.destroy()
    import login
"""

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#020E2E')
progress = Progressbar(splashscreen, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=350, mode='determinate')
progress.place(x=50,y=450)

def bar():
    a = '#249794'
    l4 = Label(splashscreen, text='Loading...', fg='white', bg="#020E2E")
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=50, y=410)

    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        splashscreen.update_idletasks()
        time.sleep(0.03)
        r = r + 1
    splashscreen.destroy()
    import login

#splashscreen.after(2000,splash1)
#splashscreen.after(2000,splash2)
splashscreen.after(500,bar)

splashscreen.mainloop()