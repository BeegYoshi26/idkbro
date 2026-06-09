from tkinter import *

class Counter:

    def __init__(self, master):
        self.master = master
        master.title("Exercise 4")

        self.count = 0
        self.label_text = IntVar()
        self.label_text.set(0)

        self.label_1 = Label(master, font = "Arial 40 bold", textvariable = self.label_text)
        self.label_1.pack()

        self.button_1 = Button(master, text="Click me", bg="black", fg="yellow", font="Arial 35 bold", command=self.click)
        self.button_1.pack(fill=X)
        
    def click(self):
        self.count += 1
        self.label_text.set(self.count)

root = Tk()
app = Counter(root)
root.mainloop()