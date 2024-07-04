import decimal
from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql
from tkinter import ttk
from decimal import Decimal


def convert():
    if toweight.get()=='' or fromweight.get()=='' or heightEntry.get()=='' :
        messagebox.showerror('Error','All fields are required')

    elif heightEntry.get().isalpha():
        messagebox.showerror('Error', 'Please enter a number')

    elif fromweight.get()=='Gram':
        if toweight.get()=='Kilogram':
            status = Decimal(float(heightEntry.get()) * 0.001)
            dec = status.quantize(decimal.Decimal('0.00'))
            r1 = str(dec) + ' KG'
            result = Label(weight, width=10, text=r1, font=('Micosoft Yahei UI Light', 18))
            result.place(x=280, y=570)
        else:
            messagebox.showerror('Error', 'Please choose the units correctly')
    elif fromweight.get()=='Kilogram':
        if toweight.get()=='Gram':
            status = Decimal(float(heightEntry.get()) * 1000)
            dec = status.quantize(decimal.Decimal('0.00'))
            r1 = str(dec) + ' Gram '
            result = Label(weight, width=10, text=r1, font=('Micosoft Yahei UI Light', 18))
            result.place(x=280, y=570)
        else:
            messagebox.showerror('Error', 'Please choose the units correctly')
def home():
    weight.destroy()
    import dashboard


weight = Tk()

weight.geometry('1300x700+50+50')
weight.resizable(0, 0)
bgImage=tk.PhotoImage(file='images/weight.png')
bgLabel=Label(weight, image=bgImage)
bgLabel.place(x=0,y=0)


#registration.title('Combobox')
n = tk.StringVar()
fromweight = ttk.Combobox(weight, width=30, textvariable=n)
fromweight['values'] = ('Gram','Kilogram')
fromweight.place(x=120, y=260)
fromweight.current()
weight.option_add('*TCombobox*Listbox.font', "35")


n = tk.StringVar()
toweight = ttk.Combobox(weight, width=30, height=30, textvariable=n)
toweight['values'] = ('Gram','Kilogram')
toweight.place(x=410, y=260)
toweight.current()
weight.option_add('*TCombobox*Listbox.font', "35")


heightEntry = Entry(weight, width=20, font=('Micosoft Yahei UI Light', 20), bd=0, background="white")
heightEntry.place(x=230,y=395)

submitbtn = Button(weight, height=2, width=15, text="Convert", background="white", activeforeground="gray", fg="black", bd=2, command=convert)
submitbtn.place(x=200,y=510)
weight.bind('<Return>',lambda event:convert())

homeb = Button(weight,height=2,width=15,text="home",background="white",activeforeground="gray",fg="black",command=home)
homeb.place(x=450,y=510)


weight.mainloop()
