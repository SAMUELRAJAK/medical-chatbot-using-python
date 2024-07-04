import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry_task.get()
    priority = var_priority.get()
    if task:
        listbox_tasks.insert(tk.END, (task, priority))  # Add task with priority to listbox
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task from the list
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear all tasks from the list
def clear_tasks():
    listbox_tasks.delete(0, tk.END)

def home():
    root.destroy()
    import dashboard

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.config(bg="#CFD1FF")

# Calculate the position for centering the window
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the geometry for centering the window
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a frame for task entry and buttons
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=20)


# Create a task entry widget
entry_task = tk.Entry(frame_tasks, width=70)
entry_task.grid(row=0, column=0, padx=5, pady=5)

# Create a priority label and dropdown menu
tk.Label(frame_tasks, text="Priority:",font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=5, pady=5)
var_priority = tk.StringVar()
priority_options = ["High", "Medium", "Low"]
priority_menu = tk.OptionMenu(frame_tasks, var_priority, *priority_options)
priority_menu.grid(row=0, column=2, padx=5, pady=5)
var_priority.set("Medium")  # Default priority

# Create an Add Task button
btn_add_task = tk.Button(frame_tasks, text="Add Task", command=add_task, bg="#4DD9D1",font=("Helvetica", 12, "bold"),fg="white")
btn_add_task.grid(row=0, column=3, padx=5, pady=5)


# Create a frame for the task list
frame_list = tk.Frame(root)
frame_list.pack(padx=20, pady=(0, 20))

# Create a task listbox
listbox_tasks = tk.Listbox(frame_list, width=100, height=20)
listbox_tasks.grid(row=0, column=0, padx=5, pady=5)

# Create a scrollbar for the task list
scrollbar_tasks = tk.Scrollbar(frame_list)
scrollbar_tasks.grid(row=0, column=1, sticky="NS")
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create a Delete Task button
btn_delete_task = tk.Button(root, text="Delete Task", command=delete_task,bg="#D82C1C",font=("Helvetica", 11, "bold"),fg="white")
btn_delete_task.place(x=350,y=450)

# Create a Clear Tasks button
btn_clear_tasks = tk.Button(root, text="Clear Tasks", command=clear_tasks,bg="#F4C189",font=("Arial", 11),fg="white")
btn_clear_tasks.place(x=150,y=450)

btn_home_tasks = tk.Button(root, text="Home", command=home,bg="#65B785",font=("Arial", 11),fg="white")
btn_home_tasks.place(x=600,y=450)
# Start the main event loop
root.mainloop()
