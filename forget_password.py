from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql

def login_page():
    forget_pass.destroy()
    import login


def forget():
    if emailEntry.get()== '' or npassEntry.get()== '' or cpassEntry.get()== '' :
        messagebox.showerror('Error','All Fields are required')
    elif npassEntry.get() != cpassEntry.get():
        messagebox.showerror('Error','Password and Confirm Password are not matching')
    else:
        con = pymysql.connect(host='localhost', user='root', password='sam',database='userdata')
        mycursor = con.cursor()
        query = 'select * from data where email=%s'
        mycursor.execute(query, (emailEntry.get()))
        row = mycursor.fetchone()

        if row == None:
            messagebox.showerror("Error","Incorrect Email"
                                         "")
        else:
            query2='update data set password=%s where username=%s'
            mycursor.execute(query2, (npassEntry.get(), emailEntry.get()))
            con.commit()
            con.commit()
            messagebox.showinfo("Success", "Password is changed, Please login with new password")
            forget_pass.destroy()
            import login

forget_pass = Tk()

forget_pass.geometry('1300x700+50+50')
forget_pass.resizable(0, 0)
bgImage=tk.PhotoImage(file='images/reset.png')

bgLabel=Label(forget_pass,image=bgImage)
bgLabel.place(x=0,y=0)

emailEntry = Entry(forget_pass, width=30, font=('Micosoft Yahei UI Bold', 20), fg="white", bd=0, background="#65B785")
emailEntry.place(x=750, y=234)

npassEntry = Entry(forget_pass,width=30,font=('Micosoft Yahei UI Bold',20),fg="white",bd=0,background="#65B785")
npassEntry.place(x=750,y=381)

cpassEntry = Entry(forget_pass,width=30,font=('Micosoft Yahei UI Bold',20),fg="white",bd=0,background="#65B785")
cpassEntry.place(x=750,y=526)

submitbtn = Button(forget_pass,text="Submit",bd=0,width=20,height=3,background="white",fg="#65B785",activeforeground="white",activebackground="#65B785",command=forget)
submitbtn.place(x=1095,y=580)
forget_pass.bind('<Return>',lambda event:forget())

forget_pass.mainloop()