from tkinter import *
from random import *

count = 0

# Quit command
def quit():
    root.destroy()

# Random command
def random():

    # count the number of times rolled
    global count
    count += 1
    label_count_num.config(text = count)

    # generate 2 random numbers
    num_1 = randint(1, 6)
    num_2 = randint(1, 6)
    # set each label to the randomly generated numbers
    label_1.config(text = num_1)
    label_2.config(text = num_2)

    # set bg to green if both are 6
    if num_1 == 6 and num_2 == 6:
        label_1.config(bg = "green")
        label_2.config(bg = "green")

    # reset to red
    else:
        label_1.config(bg = "red")
        label_2.config(bg = "red")

# define contants for styles
style = "Arial 16"

root = Tk()
root.title("Dice roll")

# set min height of all rows to 50px
root.rowconfigure([0,1,2], minsize=50, weight = 1)

# set min column width to 200px
root.columnconfigure([0,1], minsize=200, weight = 1)

# layout widgets
button_quit = Button(root, text = "Quit", font = style, command = quit)
button_quit.grid(row = 0, column = 0, sticky = "ew", padx = 10)

button_random = Button(root, text = "Random", font = style, command = random)
button_random.grid(row = 0, column = 1, sticky = "ew", padx = 10)

label_1 = Label(root, text = "", font = style, bg = "red")
label_1.grid(row = 1, column = 0, sticky = "ew", padx = 10)

label_2 = Label(root, text = "", font = style, bg = "red")
label_2.grid(row = 1, column = 1, sticky = "ew", padx = 10)

label_count = Label(root, text = "Roll count =", font = style)
label_count.grid(row = 2, column = 0, sticky = "ew", padx = 10)

label_count_num = Label(root, text = "", font = style)
label_count_num.grid(row = 2, column = 1, sticky = "ew", padx = 10)

root.mainloop()