from tkinter import *

def click():
    global count
    count += 1
    label_1.configure(text=count)

root = Tk()
root.title("Exercise 3")


count = 0


label_1 = Label(root, font = "Arial 40 bold", text = count)
label_1.pack()

button_1 = Button(root, text="Click me", bg="black", fg="yellow", font="arial 35 bold", command=click)
button_1.pack(fill=X)

root.mainloop()