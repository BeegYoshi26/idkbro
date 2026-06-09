from tkinter import *
from random import *

num = 0

# Quit command
def quit():
    root.destroy()

def random():
    global num
    num = randint(1, 10)
    label_confirm.config(text = "New Number generated", bg = "yellow")

def check():
    global num
    if int(box.get()) == num:
        label_confirm.config(text = "Correct", bg = "green")
    elif int(box.get()) > num:
        label_confirm.config(text = "Too high", bg = "red")
    elif int(box.get()) < num:
        label_confirm.config(text = "Too low", bg = "red")
    else:
        label_confirm.config(text = "ERROR", bg = "red")

style = "Arial 16"
width = 10

root = Tk()
root.title("Guess the number")

# set min height of all rows to 50px
root.rowconfigure([0,1,2], minsize= 50, weight = 1)

# set min column width to 200px
root.columnconfigure([0,1,2], minsize= 50, weight = 1)

# layout widgets
button_random = Button(root, text = "Random", font = style, width = width, command = random)
button_random.grid(row = 0, column = 0, sticky = "ew", padx = 10)

button_random = Button(root, text = "Check", font = style, width = width, command = check)
button_random.grid(row = 0, column = 1, sticky = "ew", padx = 10)

button_quit = Button(root, text = "Quit", font = style, width = width, command = quit)
button_quit.grid(row = 0, column = 2, sticky = "ew", padx = 10)

label = Label(root, text = "Guess the number", font = style)
label.grid(row = 1, column = 0, columnspan = 2, sticky = "ew", padx = 10)

box = Entry(root, font = style)
box.grid(row = 1, column = 2, sticky = "ew", padx = 10)

label_confirm = Label(root, text = "Press Random to generate a random number between 1 and 10.", font = style, bg = "yellow")
label_confirm.grid(row = 2, column = 0, columnspan = 3, sticky = "nsew")

root.mainloop()