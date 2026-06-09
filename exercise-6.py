from tkinter import *

# define contants for styles
style = "Arial 20"
background = "blue"

root = Tk()
root.title("Grid layout example")

# set min height of all rows to 50px
root.rowconfigure([0,1,2], minsize=50, weight=1)

# set min width of all columns to 200px
root.columnconfigure([0,1], minsize=200, weight=1)

# layout widgets
a = Label(root, text = "top left", bg = background, font = style)
a.grid(row = 0, column = 0)

b = Label(root, text = "top right", bg = background, font = style)
b.grid(row = 0, column = 1)

c = Label(root, text = "bottom left", bg = background, font = style)
c.grid(row = 1, column = 0)

d = Label(root, text = "bottom right", bg = background, font = style)
d.grid(row = 1, column = 1)

e = Label(root, text = "merge", bg = "pink", font = style)
e.grid(row = 2, column = 0, columnspan = 2, sticky = "we")

root.mainloop()