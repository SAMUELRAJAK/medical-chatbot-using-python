from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql

def login_page():
    signup_window.destroy()
    import login

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields are required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms and Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='sam')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table users(id int auto_increment primary key not null,email varchar(30),username varchar(30),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select * from users where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row = mycursor.fetchone()

        query = 'select * from users where email=%s'
        mycursor.execute(query, (emailEntry.get()))
        email = mycursor.fetchone()

        if row != None and email!=None:
            messagebox.showerror('Error','Username or Email ID Already Exists')
        elif email != None:
                messagebox.showerror('Error', 'Email ID Already Exists')
        elif row!=None:
            messagebox.showerror('Error', 'Username Already Exists')

        else:

            query = 'insert into users(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is successfull")
            clear()
            signup_window.destroy()
            import registration

def show():
    closeb = ImageTk.PhotoImage(file="images/eye/close.png")
    close_btn = Button(signup_window, command=hide(),image=closeb, background="white", activebackground="white")
    close_btn.place(x=350, y=350)
    passwordEntry.config(show="")
    confirmEntry.config(show="")
    print("show")

def hide():
    openb = ImageTk.PhotoImage(file="images/eye/open.png")
    open_btn = Button(signup_window, image=openb, command=show(), background="white", bd=0)
    open_btn.place(x=350, y=350)
    passwordEntry.config(show="*")
    confirmEntry.config(show="*")
    print("hide")

signup_window = Tk()

signup_window.geometry('1300x700+50+50')
signup_window.resizable(0,0)
bgImage=tk.PhotoImage(file='images/Signup.png')
bgLabel=Label(signup_window,image=bgImage)
bgLabel.place(x=0,y=0)


emailEntry = Entry(signup_window,width=20,font=('Micosoft Yahei UI Light',20),fg='white',bd=0,background="#D4CAC0")
emailEntry.place(x=170,y=185)

usernameEntry = Entry(signup_window,width=20,font=('Micosoft Yahei UI Light',20),fg='white',bd=0,background="#D4CAC0")
usernameEntry.place(x=170,y=292)

passwordEntry = Entry(signup_window,width=20,font=('Micosoft Yahei UI Light',20),fg='white',bd=0,background="#D4CAC0",show="*")
passwordEntry.place(x=170,y=400)

eye_open = ImageTk.PhotoImage(file="images/eye/open.png")
open_btn = Button(signup_window,image=eye_open,command=show,background="white",bd=0)
open_btn.place(x=350,y=350)

confirmEntry = Entry(signup_window,width=20,font=('Micosoft Yahei UI Light',20),fg='white',bd=0,background="#D4CAC0",show="*")
confirmEntry.place(x=170,y=510)

check = IntVar()
termsandcon = Checkbutton(signup_window,font=('Micosoft Yahei UI Light',13),bg="white",variable=check)
termsandcon.place(x=100,y=589)

signupbtn = tk.PhotoImage(file="images/Buttons/signupbtn.png")
signupButton = Button(signup_window,image=signupbtn,bd=0,background="white",command=connect_database)
signupButton.place(x=425,y=580)
signup_window.bind('<Return>',lambda event:connect_database())


loginButton = Button(signup_window,text="Log in",font=('Times New Romans','12','bold'),bd=0,bg="white",fg='#D4CAC0',activebackground='white',activeforeground='#A77A59'
                     ,command=login_page)
loginButton.place(x=360,y=632)



signup_window.mainloop()