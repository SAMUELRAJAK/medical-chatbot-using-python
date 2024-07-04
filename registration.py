from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql
from tkinter import ttk


def to_database():
    a = 0
    str = emailEntry.get()
    for i in str:
        if i == '@':
            a = 1

    if  nameEntry.get()=='' or ageEntry.get()=='' or addressEntry.get()=='' or groupchoosen.get()=='' or heightEntry.get()=='' or weightEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='':
        messagebox.showerror('Error','All Fields are required')

    elif len(phoneEntry.get()) != 10:
        messagebox.showerror('Error',"Enter a valid mobile number")

    elif a == 0:
        messagebox.showerror("Error", "Enter a valid email id")

    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='sam')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table userdetails(username varchar(20),age int(3),address varchar(25),height int(3),weight int(3),bgroup varchar(4),phone int(10),email varchar(10))'
            mycursor.execute(query)
        except:
            query = 'use userdata'
            mycursor.execute(query)
            query = 'select * from users where email=%s'
            mycursor.execute(query, (emailEntry.get()))
            row = mycursor.fetchone()

            if row != None :
                query = 'insert into userdetails(username,age,address,height,weight,bgroup,phone,email) values(%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (nameEntry.get(), ageEntry.get(),addressEntry.get(),heightEntry.get(), weightEntry.get(),groupchoosen.get(),phoneEntry.get(),emailEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration is successfull")
                registration.destroy()
                import dashboard
            else:
                messagebox.showerror('Error', 'Please Signup yourself')
                registration.destroy()
                import login


registration = Tk()
registration.geometry('1300x700+50+50')
registration.resizable(0,0)
bgImage=tk.PhotoImage(file='images/register.png')
bgLabel=Label(registration,image=bgImage)
bgLabel.place(x=0,y=0)


# to fetch user id from "data" table
con = pymysql.connect(host='localhost',user='root',password='sam')
mycursor1 = con.cursor()
query = 'use userdata'
mycursor1.execute(query)


nameEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Bold',20),bd=0,background="white")
nameEntry.place(x=116,y=201)

ageEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
ageEntry.place(x=500,y=208)

addressEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
addressEntry.place(x=880,y=208)

heightEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
heightEntry.place(x=115,y=382)

weightEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
weightEntry.place(x=500,y=388)

#registration.title('Combobox')
n = tk.StringVar()
groupchoosen = ttk.Combobox(registration, width=40, textvariable=n)
groupchoosen['values'] = (' A+',' A-',' B+',' B-',' O+',' O-',' AB+',' AB-')
groupchoosen.place(x=900,y=388)
groupchoosen.current()
registration.option_add('*TCombobox*Listbox.font', "35")

phoneEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
phoneEntry.place(x=118,y=565)

emailEntry = Entry(registration,width=20,font=('Micosoft Yahei UI Light',20),bd=0,background="white")
emailEntry.place(x=500,y=571)

submitbtn = tk.PhotoImage(file="images/Buttons/submit.png")
submitbtn1 = Button(registration,image=submitbtn,bd=0,command=to_database,background="#E7F5FD")
submitbtn1.place(x=920,y=560)
registration.bind('<Return>',lambda event:to_database())

def home():
    registration.destroy()
    import dashboard

homebtn = tk.PhotoImage(file="images/Buttons/home.png")
homebtn1 = Button(registration,image=homebtn,bd=0,background="#E7F5FD",command=home)
homebtn1.place(x=1100,y=560)


registration.mainloop()