from tkinter import *
from random import *

# initiate class
class Dice:

    def __init__(self, root):
        self.root = root
        self.root.title("Dice roll")

        self.count = 0
        self.style = "Arial 16"

        # set min height of all rows to 50px
        self.root.rowconfigure([0,1,2], minsize=50, weight = 1)

        # set min column width to 200px
        self.root.columnconfigure([0,1], minsize=200, weight = 1)

        self.create_widgets()

    # layout widgets
    def create_widgets(self):
        self.button_quit = Button(root, text = "Quit", font = self.style, command = self.quit)
        self.button_quit.grid(row = 0, column = 0, sticky = "ew", padx = 10)

        self.button_random = Button(root, text = "Random", font = self.style, command = self.roll )
        self.button_random.grid(row = 0, column = 1, sticky = "ew", padx = 10)

        self.label_1 = Label(root, text = "", font = self.style, bg = "red")
        self.label_1.grid(row = 1, column = 0, sticky = "ew", padx = 10)

        self.label_2 = Label(root, text = "", font = self.style, bg = "red")
        self.label_2.grid(row = 1, column = 1, sticky = "ew", padx = 10)

        self.label_count = Label(root, text = "Roll count =", font = self.style)
        self.label_count.grid(row = 2, column = 0, sticky = "ew", padx = 10)

        self.label_count_num = Label(root, text = "", font = self.style)
        self.label_count_num.grid(row = 2, column = 1, sticky = "ew", padx = 10)

    # Quit command
    def quit(self):
        self.root.destroy()

    # Random command
    def roll(self):

        # count the number of times rolled
        self.count += 1
        self.label_count_num.config(text = self.count)

        # generate 2 random numbers
        num_1 = randint(1, 6)
        num_2 = randint(1, 6)
        # set each label to the randomly generated numbers
        self.label_1.config(text = num_1)
        self.label_2.config(text = num_2)

        # set bg to green if both are 6
        if num_1 == 6 and num_2 == 6:
            self.label_1.config(bg = "green")
            self.label_2.config(bg = "green")
            self.count = 0
            self.label_count_num.config(text = "0")

        # reset to red
        else:
            self.label_1.config(bg = "red")
            self.label_2.config(bg = "red")

        # define contants for styles

# execute program
if __name__ == "__main__":
    root = Tk()
    app = Dice(root)
    root.mainloop()