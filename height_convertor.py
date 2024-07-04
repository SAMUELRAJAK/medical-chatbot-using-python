import decimal
from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql
from tkinter import ttk
from decimal import Decimal

def convert():
    if fromheight.get()=='':
        messagebox.showerror('Error', 'All Fields are required')
    elif fromheight.get()=='cm':
        if toheight.get()=='m':
            status = Decimal(float(heightEntry.get()) * 0.01)
            dec = status.quantize(decimal.Decimal('0.00'))
            r1=str(dec)+' metre'
            result = Label(height,width=10,text=r1,font=('Micosoft Yahei UI Light',18),background="#D1CDCD")
            result.place(x=765,y=570)
        elif toheight.get()=='feet':
            status = Decimal(float(heightEntry.get()) * 0.0328084)
            dec = status.quantize(decimal.Decimal('0.00'))
            r2=str(dec)+' feet'
            result = Label(height,width=10,text=r2,font=('Micosoft Yahei UI Light',18),background="#D1CDCD")
            result.place(x=765,y=570)
        else:
            messagebox.showerror('Error', 'Please choose the units correctly')

    elif fromheight.get()=='m':
        if toheight.get()=='cm':
            status = Decimal(float(heightEntry.get()) * 100)
            dec = status.quantize(decimal.Decimal('0.00'))
            r3=str(dec)+' cm'
            result = Label(height,width=10,text=r3,font=('Micosoft Yahei UI Light',18),background="#D1CDCD")
            result.place(x=765,y=570)
        elif toheight.get()=='feet':
            status = Decimal(float(heightEntry.get()) * 3.281)
            dec = status.quantize(decimal.Decimal('0.00'))
            r4=str(dec)+' feet'
            result = Label(height,width=10,text=r4,font=('Micosoft Yahei UI Light',18),background="#D1CDCD")
            result.place(x=765,y=570)
        else:
            messagebox.showerror('Error', 'Please choose the units correctly')

    elif fromheight.get()=='feet':
        if toheight.get()=='cm':
            status = Decimal(float(heightEntry.get()) * 30.48)
            dec = status.quantize(decimal.Decimal('0.00'))
            r5=str(dec)+' cm'
            result = Label(height,width=10,text=r5,font=('Micosoft Yahei UI Light',18),background="#D1CDCD")
            result.place(x=765,y=570)
        elif toheight.get()=='m':
            status = Decimal(float(heightEntry.get()) * 0.3048)
            dec = status.quantize(decimal.Decimal('0.00'))
            r6=str(dec)+' metre'
            result = Label(height,width=10,text=r6,font=('Micosoft Yahei UI Light',18),background="#D1CDCD")
            result.place(x=765,y=570)
        else:
            messagebox.showerror('Error', 'Please choose the units correctly')

def home():
    height.destroy()
    import dashboard

height = Tk()

height.geometry('1300x700+50+50')
height.resizable(0, 0)
bgImage=tk.PhotoImage(file='images/height.png')
bgLabel=Label(height, image=bgImage)
bgLabel.place(x=0,y=0)


#registration.title('Combobox')
n = tk.StringVar()
fromheight = ttk.Combobox(height, width=30, textvariable=n)
fromheight['values'] = ('cm','m','feet')
fromheight.place(x=590,y=280)
fromheight.current()
height.option_add('*TCombobox*Listbox.font', "35")


n = tk.StringVar()
toheight = ttk.Combobox(height, width=30,height=20, textvariable=n)
toheight['values'] = ('cm','m','feet')
toheight.place(x=930,y=280)
toheight.current()
height.option_add('*TCombobox*Listbox.font', "35")

heightEntry = Entry(height,width=15,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
heightEntry.place(x=740,y=388)

submitbtn = Button(height,height=2,width=15,text="Convert",background="white",activeforeground="gray",fg="black",bd=2,command=convert)
submitbtn.place(x=800,y=480)
height.bind('<Return>',lambda event:convert())

homeb = Button(height,height=2,width=10,text="home",background="white",activeforeground="gray",fg="black",command=home)
homeb.place(x=950,y=580)


height.mainloop()
