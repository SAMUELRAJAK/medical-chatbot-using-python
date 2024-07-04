from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql
#from tkinter import ttk

def calculate():
    if heightEntry.get()=="" or WeightEntry.get()=="" :
        messagebox.showerror("Error","All fields are required")
    else:
        h = int(heightEntry.get())
        w = int(WeightEntry.get())
        res = w / (h * h)
        bmi = res * 10000

        if (bmi < 18.5):
            status = "Your BMI Value : " + str(bmi) + "\nBody Status is UnderWeight"
        elif (bmi >= 18.5 and bmi <= 24.9):
            status = "Your BMI Value : " + str(bmi) + "\nBody Status is Normal Weight"
        elif (bmi >= 25 and bmi <= 29.9):
            status = "Your BMI Value : " + str(bmi) + "\nBody Status is OverWeight"
        elif (bmi >= 30):
            status = "Your BMI Value : " + str(bmi) + "\nBody Status is Obese"
        else:
            status = "Invalid inputs"

        bmiLabel = Label(BMI, text=status, font=('Micosoft Yahei UI Light', 18), background="#D1CDCD")
        bmiLabel.place(x=460, y=570)

def dashboard():
    BMI.destroy()
    import dashboard

BMI = Tk()

BMI.geometry('1300x700+50+50')
BMI.resizable(0, 0)
bgImage=tk.PhotoImage(file='images/Bmi calculator.png')
bgLabel=Label(BMI,image=bgImage)
bgLabel.place(x=0,y=0)


ageEntry = Entry(BMI,width=13,font=('Micosoft Yahei UI Light',20),fg='black',bd=0,background="white")
ageEntry.place(x=880,y=165)

GenderEntry = Entry(BMI,width=13,font=('Micosoft Yahei UI Light',20),fg='black',bd=0,background="white")
GenderEntry.place(x=880,y=262)

heightEntry = Entry(BMI,width=13,font=('Micosoft Yahei UI Light',20),fg='black',bd=0,background="white")
heightEntry.place(x=880,y=363)

WeightEntry = Entry(BMI,width=13,font=('Micosoft Yahei UI Light',20),fg='black',bd=0,background="white")
WeightEntry.place(x=880,y=453)


calculatebtn = tk.PhotoImage(file="images/Buttons/calculate.png")
calbtn = Button(BMI,image=calculatebtn,bd=0,background="#C8C8C8",activebackground="#C8C8C8",command=calculate)
calbtn.place(x=970,y=530)


backbtnn = tk.PhotoImage(file="images/Buttons/back.png")
backbtn = Button(BMI,image=backbtnn,bd=0,background="#D1CDCD",activebackground="#D1CDCD",command=dashboard)
backbtn.place(x=1100,y=600)
BMI.bind('<Return>',lambda event:calculate())



BMI.mainloop()


