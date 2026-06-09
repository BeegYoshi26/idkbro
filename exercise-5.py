from tkinter import *

# Quit command
def quit():
    root.destroy()

# Print command
def print_text():
    try:
        # add both entry values
        total = int(box.get()) + int(box2.get())

        # set result label to total
        result_label.config(text = str(total))

    # give error if invalid entry
    except ValueError:
        result_label.config(text = str("ERROR"))


# Reset command
def reset():
    # reset the entry boxes
    box.delete(0, END)
    box2.delete(0, END)

    # reset result label
    result_label.config(text = "")

# Root
root = Tk()
root.title("Exercise 5")
root.resizable(0,0)

# Num 1 entry
box = Entry(root, justify = CENTER, font = ("Arial", 14))
box.pack(fill = X, ipady = 10)

# Plus sign label
label = Label(root, text = "+", font = ("Arial", 24))
label.pack(fill = X, ipady = 10)

# Num 2 entry
box2 = Entry(root, justify = CENTER, font = ("Arial", 14))
box2.pack(fill = X, ipady = 10)

# Result label
result_label = Label(root, text = "", font = ("Arial", 24))
result_label.pack(fill = X, ipady = 10)

# Print button
button_print = Button(root, text = "Print", width = 10, command = print_text)
button_print.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

# Reset button
button_reset = Button(root, text = "Reset", width = 10, command = reset)
button_reset.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

# Quit button
button_quit = Button(root, text = "Quit", width = 10, command = quit)
button_quit.pack(side = LEFT, ipady = 10, padx = 10, pady = 10)

root.mainloop()