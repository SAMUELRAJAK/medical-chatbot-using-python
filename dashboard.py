from tkinter import *
from PIL import ImageTk
import tkinter as tk
from tkinter  import messagebox
import pymysql
from tkinter import ttk
import time
import random

dashboard = Tk()

dashboard.geometry('1300x700+50+50')
dashboard.resizable(0, 0)
bgImage=tk.PhotoImage(file='images/dashboard.png')
bgLabel=Label(dashboard,image=bgImage)
bgLabel.place(x=0,y=0)

from datetime import date

# Returns the current local date
today = date.today()
#print("Today date is: ", today)
dateEntry = Label(dashboard, width=10, text=today, font=('Times New Roman bold', 20),background="#4DD9D1",fg="white")
dateEntry.place(x=1050, y=27)

# Create a styled button
styled_button = tk.Button(dashboard, text="Click Me", bg="white", fg="#4DD9D1", font=("Helvetica", 12), bd=0, relief=tk.RAISED)
styled_button.place(x=20, y=300)


def digitalclock():
   text_input = "Time : "+ time.strftime("%H:%M:%S")
   timeLabel = Label(text=text_input,fg="white",bg="#4DD9D1", font=("Times New Roman bold", 20), bd=0, relief=tk.RAISED)
   timeLabel.place(x=20,y=200)
   timeLabel.after(200, digitalclock)
digitalclock()

icon = tk.PhotoImage(file="images/icon.png")
chatbot = Button(dashboard,image=icon,bd=0,background="#4DD9D1",activebackground="#4DD9D1",height=200,width=200)

chatbot.place(x=10,y=5)

def greetings():
   h = int(time.strftime("%H"))
   m = int(time.strftime("%M"))
   s = int(time.strftime("%S"))
   textt=""
   if (h <= 12 or (h <= 12 and m <= 59)):
      textt = "Good Morning!!! \n      Wellness Seekers!!"
   elif (h >= 12 or (h >= 12 and m >= 1)) and h <= 16:
      textt = "Good Afternoon!!! \n    Health Fanatics!!"
   elif (h >= 21):
      textt = "Good Night!!! \n   Fitness Freaks!!"
   textl = Label(text=textt, fg="white", bg="#4DD9D1", font=("Times New Roman bold", 17), bd=0, relief=tk.RAISED)
   textl.place(x=15, y=300)
greetings()


#VOICE ASSISTANT
def search():
   import speech_recognition as sr
   import webbrowser
   import openai
   import cv2

   sr.Microphone(device_index=0)
   r = sr.Recognizer()
   r.energy_threshold = 5000

   with sr.Microphone() as source:
      audio = r.listen(source)
      try:
         text = r.recognize_google(audio)
         #print("You said:{}".format(text))
         url = "https://www.google.com/search?q="
         search_url = url + text
         webbrowser.open(search_url)
      except:
         askLabel = Label(dashboard, text="Speak Again!!", background="#4DD9D1", fg="white", bd=0,
                          font=("Times New Roman bold", 16))
         askLabel.place(x=60, y=654)
         ask.place(x=25, y=650)

#ASK GOOGLE
mike = tk.PhotoImage(file="images/Buttons/micrphone.png")
ask = Button(dashboard,image=mike,bd=0,command=search,background="#4DD9D1",activebackground="#4DD9D1")
askLabel = Label(dashboard,text="Ask google!!",background="#4DD9D1",fg="white",bd=0,font=("Times New Roman bold", 16))
askLabel.place(x=60,y=654)
ask.place(x=25,y=650)

def calender():
    from tkcalendar import Calendar
    from datetime import datetime

    # Get today's date
    today = datetime.now().date()

    # Create a Year Calendar widget with a larger font size and different background color
    cal = Calendar(selectmode="day", year=datetime.now().year, background="#638BBF", foreground="white",
                   font=('Helvetica', 8), selectbackground="yellow", selectforeground="black",
                   date_pattern="yyyy-mm-dd")

    # Highlight today's date
    cal.tag_config("today", background="red", foreground="white")
    cal.calevent_create(today, "Today", "today")

    # Place the calendar widget
    cal.place(x=15,y=430)


calender()

def update_health_quotes(text_widget):
   # Health quotes
   health_quotes = [
    "Take care of your body. It's the only place you have to live. - Jim Rohn",
    "Health is a state of complete harmony of the body, mind, and spirit. - B.K.S. Iyengar",
    "The greatest wealth is health. - Virgil",
    "Good health is not something we can buy. However, it can be an extremely valuable savings account. - Anne Wilson Schaef",
    "The first wealth is health. - Ralph Waldo Emerson",
    "To ensure good health: eat lightly, breathe deeply, live moderately, cultivate cheerfulness, and maintain an interest in life. - William Londen",
    "An apple a day keeps the doctor away.",
    "Your body hears everything your mind says.",
    "The doctor of the future will no longer treat the human frame with drugs, but rather will cure and prevent disease with nutrition. - Thomas Edison",
    "The mind and body are not separate. What affects one, affects the other.",
    "Happiness is the highest form of health.",
    "Health is not simply the absence of sickness. - Hannah Green",
    "A healthy outside starts from the inside. - Robert Urich",
    "Those who think they have no time for healthy eating will sooner or later have to find time for illness. - Edward Stanley",
    "Let food be thy medicine and medicine be thy food. - Hippocrates",
    "The groundwork of all happiness is health. - Leigh Hunt",
    "The greatest wealth is health. - Virgil",
    "Health is like money, we never have a true idea of its value until we lose it. - Josh Billings",
    "Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity. - John F. Kennedy",
    "The doctor of the future will give no medicine, but will instruct his patients in care of the human frame, in diet, and in the cause and prevention of disease. - Thomas Edison"
]

   # Choose a random health quote
   random_quote = random.choice(health_quotes)

   # Update the text widget
   text_widget.config(state=tk.NORMAL)  # Set text widget to normal state to allow editing
   text_widget.delete('1.0', tk.END)  # Clear existing text
   text_widget.insert(tk.END, random_quote)  # Insert random quote
   text_widget.config(state=tk.DISABLED)  # Set text widget back to disabled state



# Create a text widget to display health quotes
text_widget = tk.Text(dashboard, font=('Arial', 14,'italic'), wrap=tk.WORD, state=tk.DISABLED,bd=0,background="#B7C7CF",fg="black")
text_widget.place(x=340, y=605, width=900, height=60)
# Function to update health quotes every 5 seconds
def update_quotes():
   update_health_quotes(text_widget)
   dashboard.after(10000, update_quotes)
update_quotes()

#All buttons functionalities

def register():
    dashboard.destroy()
    import registration
def bmi():
    dashboard.destroy()
    import bmi_calculator

def chat():
    dashboard.destroy()
    import chat

def todolist():
    dashboard.destroy()
    import todo

def notes():
    dashboard.destroy()
    import notes

def height():
    dashboard.destroy()
    import height_convertor

def weight():
    dashboard.destroy()
    import weight_convertor

def quotes1():
    #dashboard.destroy()
    import quotes

regisbtn = tk.PhotoImage(file="images/Buttons/register.png")
registerbtn = Button(dashboard,image=regisbtn,bd=0,command=register,bg="#4DD9D1",activebackground="#4DD9D1")
registerbtn.place(x=369,y=206)

chatbtn = tk.PhotoImage(file="images/Buttons/chat.png")
CHATbtn = Button(dashboard,image=chatbtn,bd=0,bg="#4DD9D1",activebackground="#4DD9D1",command=chat)
CHATbtn.place(x=635,y=203)

todobtn = tk.PhotoImage(file="images/Buttons/todolist.png")
todolistbtn = Button(dashboard,image=todobtn,bd=0,bg="#4DD9D1",activebackground="#4DD9D1",command=todolist)
todolistbtn.place(x=893,y=203)


notebtn = tk.PhotoImage(file="images/Buttons/notes.png")
notesbtn = Button(dashboard,image=notebtn,bd=0,bg="#4DD9D1",activebackground="#4DD9D1",command=notes)
notesbtn.place(x=1158,y=203)

bmibtn = tk.PhotoImage(file="images/Buttons/bmi.png")
BMIbtn = Button(dashboard,image=bmibtn,bd=0,command=bmi,bg="#4DD9D1",activebackground="#4DD9D1")
BMIbtn.place(x=369,y=382)

heightbtn = tk.PhotoImage(file="images/Buttons/height.png")
hbtn = Button(dashboard,image=heightbtn,bd=0,command=height,bg="#4DD9D1",activebackground="#4DD9D1")
hbtn.place(x=630,y=389)

weightbtn = tk.PhotoImage(file="images/Buttons/weight.png")
wbtn = Button(dashboard,image=weightbtn,bd=0,command=weight,bg="#4DD9D1",activebackground="#4DD9D1")
wbtn.place(x=893,y=389)

quotestbtn = tk.PhotoImage(file="images/Buttons/quotes.png")
wbtn = Button(dashboard,image=quotestbtn,bd=0,command=quotes1,bg="#4DD9D1",activebackground="#4DD9D1")
wbtn.place(x=1158,y=389)

dashboard.mainloop()


