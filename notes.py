import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def save_note():
    note = text.get("1.0", tk.END)
    with open("notes.txt", "w") as file:
        file.write(note)
    messagebox.showinfo("Note Saved", "Your note has been saved successfully!")

def clear_note():
    text.delete("1.0", tk.END)

def home():
    root.destroy()
    import dashboard

root = tk.Tk()
root.title("Note Taking App")
root.geometry("1300x700")

# Load the image
bg_image = Image.open("images/notes.png")
# Resize the image to fit the window size
bg_image_resized = bg_image.resize((1300, 700))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

# Create a label to hold the image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

text = tk.Text(root, wrap="word", height=28, width=55, bg="white", font=("Helvetica", 12))

text.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

try:
    with open("notes.txt", "r") as file:
        saved_notes = file.read()
        text.insert(tk.END, saved_notes)
except FileNotFoundError:
    pass

save_button = tk.Button(root, text="Save Note", command=save_note, bg="#4CAF50", fg="white")
save_button.place(relx=0.4, rely=0.85, anchor=tk.CENTER)

clear_button = tk.Button(root, text="Clear Note", command=clear_note, bg="#FF5733", fg="white")
clear_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

back_button = tk.Button(root, text="Home", command=home, bg="#826DE4", fg="white")
back_button.place(relx=0.6, rely=0.85, anchor=tk.CENTER)

root.mainloop()
