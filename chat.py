import tkinter
from tkinter import *
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
from tkinter import filedialog
from tkinter import messagebox

# Load pre-trained model and data
model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define functions to clean up sentence and create bag of words
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)

# Define function to predict intent
def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Define function to get response based on predicted intent
def getResponse(ints, intents_json):
    if not ints:  # Check if the list is empty
        return "Sorry, I didn't understand that."
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


# Define function to generate chatbot response
def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res

# Define function to send message and get response
def send(event=None):
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

# Define function to clear chat
def clear_chat():
    ChatLog.config(state=NORMAL)
    ChatLog.delete('1.0', END)
    ChatLog.config(state=DISABLED)

# Define function to save chat to txt file
def save_chat():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, "w") as f:
            f.write(ChatLog.get("1.0", END))

# Define function to change theme
def change_theme(theme):
    chat.configure(bg=theme['bg'])
    ChatLog.configure(bg=theme['bg'], fg=theme['fg'], insertbackground=theme['fg'])
    EntryBox.configure(bg=theme['entry_bg'], fg=theme['fg'])
    SendButton.configure(bg=theme['button_bg'])

# Create GUI window
chat = Tk()
chat.title("Medibot")
chat.geometry("500x500")  # Set window size to 500x500
chat.resizable(width=FALSE, height=FALSE)

chat.iconbitmap("images/Buttons/images_Ov7_2.ico")
# Create Chat window
ChatLog = Text(chat, bd=0, bg="white", height="8", width="50", font="Arial")
ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(chat, command=ChatLog.yview, cursor="spider")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(chat, font=("Verdana", 14, 'bold'), text="Send", width="10", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command= send)
chat.bind('<Return>', send)

# Create the box to enter message
EntryBox = Text(chat, bd=0, bg="white", width="29", height="5", font="Arial")

# Place all components on the screen
scrollbar.place(x=476,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=470)
EntryBox.place(x=128, y=401, height=90, width=345)
SendButton.place(x=6, y=401, height=90)

# Define color themes
theme1 = {'bg': 'white', 'fg': 'black', 'entry_bg': 'white', 'button_bg': '#32de97'}
theme2 = {'bg': 'black', 'fg': 'black', 'entry_bg': 'white', 'button_bg': '#ff5733'}
theme3 = {'bg': '#3498db', 'fg': 'white', 'entry_bg': '#2980b9', 'button_bg': '#d35400'}
theme4 = {'bg': '#2ecc71', 'fg': 'white', 'entry_bg': '#27ae60', 'button_bg': '#494C50'}
theme5 = {'bg': '#FFD7C4', 'fg': 'black', 'entry_bg': '#FFF6E9', 'button_bg': '#A77A59'}

# Function to change theme
def change_theme_menu(theme):
    change_theme(theme)

def dashboard():
    chat.destroy()
    import dashboard
# Create Menu
menu = Menu(chat)
chat.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Clear Chat", command=clear_chat)
file_menu.add_command(label="Save Chat", command=save_chat)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=dashboard)

theme_menu = Menu(menu)
menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Normal", command=lambda: change_theme_menu(theme1))
theme_menu.add_command(label="Coder", command=lambda: change_theme_menu(theme2))
theme_menu.add_command(label="Aquatic", command=lambda: change_theme_menu(theme3))
theme_menu.add_command(label="Nature", command=lambda: change_theme_menu(theme4))
theme_menu.add_command(label="Pearl", command=lambda: change_theme_menu(theme5))

about_menu = Menu(menu)
menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About Medibot", command=lambda: messagebox.showinfo("About", "This is a chatbot created using tkinter and trained with a neural network."))
about_menu.add_command(label="Developer", command=lambda: messagebox.showinfo("Developer", "Developed by Samuel Raja K"))


chat.mainloop()
