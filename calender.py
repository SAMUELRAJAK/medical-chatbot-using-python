import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

def get_today_date():
    today_date = datetime.now().strftime("%Y-%m-%d")
    label_today.config(text="Today's Date: " + today_date)

root = tk.Tk()
root.title("Year Calendar")
root.configure(bg="#007bff")

# Create a Year Calendar widget with a larger font size and different background color
cal = Calendar(root, selectmode="day", year=datetime.now().year, background="#f0f0f0", foreground="black", font=('Helvetica', 14))
cal.pack(pady=20)

# Button to get today's date
btn_today_date = ttk.Button(root, text="Today's Date", command=get_today_date, style='Blue.TButton')
btn_today_date.pack(pady=10)

# Label to display today's date
label_today = tk.Label(root, text="Today's Date: ", bg="#007bff", fg="white", font=('Helvetica', 12, 'bold'))
label_today.pack(pady=10)

# Customizing the Button Style
s = ttk.Style()
s.configure('Blue.TButton', foreground='white', background='#007bff')

root.mainloop()
