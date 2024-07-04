from tkinter import *
from PIL import ImageTk
import tkinter as tk
import pymysql
from tkinter  import messagebox

#Functionality part
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='password':
        passwordEntry.delete(0,END)

def signup_page():
    root.destroy()
    import signup

def chat():
    root.destroy()
    import main

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='sam')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)

        query = 'select * from users where email=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=  mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Success','Logged in Successfully')
            root.destroy()
            import dashboard

def main():
    root.destroy()
    import main


def forgetpass():
    root.destroy()
    import forget_password

#GUI PART
root = Tk()

root.geometry('1300x700+50+50')
root.resizable(0,0)
bgImage=tk.PhotoImage(file='images/login.png')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

usernameEntry = Entry(root,width=20,font=('Micosoft Yahei UI Light',20),fg='white',bd=0,background="#4DD9D1")
usernameEntry.place(x=120,y=270)

passwordEntry = Entry(root,width=20,font=('Micosoft Yahei UI Light',20),fg='white',bd=0,background="#4DD9D1")
passwordEntry.place(x=120,y=380)

fpassbtn =tk.PhotoImage(file='images/Buttons/Forget Password.png')
forgotpassbtn = Button(root,image=fpassbtn,bd=0,background="white",command=forgetpass)
forgotpassbtn.place(x=290,y=440)

loginbtn =tk.PhotoImage(file='images/Buttons/Loginbtn.png')
loginButton = Button(root,image=loginbtn,bd=0,bg="white",fg='blue',activebackground='white',activeforeground='blue',command=login_user)
loginButton.place(x=100,y=500)
root.bind('<Return>',lambda event:login_user())

signupButton = Button(root,text="Signup",font=('Times New Romans','15','bold underline'),bd=0,bg="white",fg='#4DD9D1',activebackground='white',activeforeground="cyan"
                     ,command=signup_page)
signupButton.place(x=280,y=593)

root.mainloop()