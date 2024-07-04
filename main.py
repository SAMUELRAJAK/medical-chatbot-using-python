import os
import openai
from openai import OpenAI
from tkinter import *
import tkinter as tk
from PIL import ImageTk
from tkinter.scrolledtext import ScrolledText
from tkinter  import messagebox
def generate():
    if userEntry.get() == '':
        messagebox.showerror('Error', 'Please  you message....')
    else:

        userinput = userEntry.get()
        print(userinput)
        client = OpenAI(api_key="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")
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": userinput}
            ], temperature=0.7)


        answer = completion.choices[0].message.content
        answer1 = ''
        for i in answer:
            answer1 += i
            if i == '. ':
                answer1 += '\n'
            elif len(answer1)>=400:
                answer1 += '\n'

        print(answer1)

        result = Label(root, text=answer1, font=('Micosoft Yahei UI Light', 13), fg='black', bd=0, background="white")
        result.place(x=20, y=20)
        #result.destroy()


root = Tk()
root.geometry('1300x700+50+50')
root.resizable(0,0)

bgImage=tk.PhotoImage(file='images/chat.png')

bgLabel=Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

userEntry = Entry(root,width=30,font=('Micosoft Yahei UI Light',17),fg='black',bd=0,background="white")
userEntry.place(x=650,y=610)

button = Button(root,text="chat",font=('Open Sans Bold',' 10'),bd=0,width=10,height=3,bg="white",fg='blue',activebackground='white',activeforeground='blue',command=generate)
button.place(x=1150,y=610)
root.bind('<Return>',lambda event:generate())


#result = Text(height=15,width=50,font=('Micosoft Yahei UI Light',13),fg='white',bd=0,background="blue",padx=10,pady=10)
#result.place(x=80,y=300)

root.mainloop()