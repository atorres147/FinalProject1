"""
Author: Ashley Torres
Date Written: 07/01/2024
Assignment: Final Project
Short Desc: To Do List
"""
import tkinter 
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
#Create functions
    
def update_listbox():
    #Clear the current list
    clear_listbox()
    #Populate the list box
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    #Get the task to add
    task = txt_input.get()
    #Make sure task list is not empty
    if task !="":
        #Append to the list
        tasks.append(task)
        #Update the listbox
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task"
    txt_input.delete(0, "end")



def label():
    #Creating image to add onto task
    img = tkinter.PhotoImage(file="motivgif.gif")

def alph_task():
    #Creating the list in alphabetical order
    tasks.sort()
    update_listbox()

def mark_done():
    try:
        chosen_index = lb_tasks.curselection()[0]
        task,done = tasks[chosen_index]
        tasks[chosen_index] = [task, True]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "No task selected")
        update_listbox()

def num_task():
    num_task = len(tasks)
    msg = "Total number of tasks: %s" %num_task
    #Display the message
    lbl_display["text"]=msg

def delete_all():
    #Since we are changing list it needs to be globsl
    global tasks
    #Clear the tasks list
    tasks = []
    #Update the list box
    update_listbox()

def del_one():
    #Get the text of the currently selected to delete 1 item
    task = lb_tasks.get("active")
    #Confrim it is in the list
    if task in task:
        tasks.remove(task)
    update_listbox()

def motive_task():
    messagebox.showinfo("Surprise", "Keep it up, You will have an amazing day")
    try:
        img = Image.open(image_path)
        img = img.resize((100, 100), Image.ANTIALIAS)  # Resize if necessary
        img = ImageTk.PhotoImage(img)
        lbl_img.config(image=img)
        lbl_img.image = img  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error loading image: {e}")
    update_listbox

def exit_all():
    root.quit()

#Create root window
root = tkinter.Tk()

#Change root window background color
root.configure(bg="white")


#Change the title
root.title("My super to do list")

#Change the window size
root.geometry("300x300")

#Creat an empty list
tasks = []

#Creating the functions
lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="Create a Productive Day", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15 )
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_alph_task = tkinter.Button(root, text="List in Alphabetical order", fg="pink", bg="white", command=alph_task)
btn_alph_task.grid(row=2,column=0)

btn_mark_done = tkinter.Button(root, text="Mark as Done", fg="blue", bg="white", command=mark_done)
btn_mark_done.grid(row=3,column=0)

btn_num_task = tkinter.Button(root, text="Total number of tasks", fg="purple", bg="white", command=num_task)
btn_num_task.grid(row=4,column=0)

btn_delete_all  = tkinter.Button(root, text="DELETE ALL", fg="red", bg="white", command=delete_all)
btn_delete_all.grid(row=5,column=0)

btn_del_one  = tkinter.Button(root, text="Delete One", fg="red", bg="white", command=del_one)
btn_del_one.grid(row=6,column=0)

btn_motive_task = tkinter.Button(root, text="Click here for a surprise", fg="blue", bg="white", command=motive_task)
btn_motive_task.grid(row=7,column=0)


btn_exit_all  = tkinter.Button(root, text="Exit List", fg="green", bg="white", command=exit_all)
btn_exit_all.grid(row=8,column=0)

lbl_img = tkinter.Label(root, bg="white")
lbl_img.grid(row=9, column=0, columnspan=2, pady=10)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)


#Start the main loop of events
root.mainloop()
