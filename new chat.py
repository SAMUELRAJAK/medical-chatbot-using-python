# Create GUI window
base = Tk()
base.title("Chatbot")
base.geometry("500x500")  # Set window size to 500x500
base.resizable(width=FALSE, height=FALSE)

# Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="spider")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= send)
base.bind('<Return>',lambda event:send())
# Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

# Place all components on the screen
scrollbar.place(x=476,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=470)
EntryBox.place(x=128, y=401, height=90, width=345)
SendButton.place(x=6, y=401, height=90)

# Create Menu
menu = Menu(base)
base.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Chat", command=save_chat)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=base.quit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear Chat", command=clear_chat)

help_menu = Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about_dialog)

base.mainloop()
