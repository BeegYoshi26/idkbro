from tkinter import *
from tkinter import ttk

class Generator:
    def __init__(self, root):
        self.root = root
        self.root.title("Superhero name generator")

        self.root.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=10, weight=1)

        self.root.columnconfigure(0, minsize=200, weight = 1)

        self.create_widgets()

    def create_widgets(self):

        self.adjective_lbl = Label(self.root, text = "Choose an adjective...")
        self.adjective_lbl.grid(row = 0, column = 0, sticky = "ew", padx = 10)

        radio_var = StringVar(value = "")

        self.option1 = ttk.Radiobutton(self.root, text = "Happy", value="Happy", variable = radio_var)
        self.option2 = ttk.Radiobutton(self.root, text = "Awesome", value="Awesome", variable = radio_var)
        self.option3 = ttk.Radiobutton(self.root, text = "Outgoing", value="Outgoing", variable = radio_var)
        self.option4 = ttk.Radiobutton(self.root, text = "Funky", value="Funky", variable = radio_var)

        self.selected_var = radio_var.get()        

        self.option1.grid(row = 1, column = 0, sticky = "ew", padx = 10)
        self.option2.grid(row = 2, column = 0, sticky = "ew", padx = 10)
        self.option3.grid(row = 3, column = 0, sticky = "ew", padx = 10)
        self.option4.grid(row = 4, column = 0, sticky = "ew", padx = 10)

        self.colour_lbl = Label(self.root, text = "Enter a colour")
        self.colour_lbl.grid(row = 5, column = 0, sticky = "ew", padx = 10)

        self.box = Entry(self.root, justify = CENTER, font = ("Arial", 14))
        self.box.grid(row = 6, column = 0, sticky = "ew", padx = 10)

        self.colour = self.box.get()

        self.animal_lbl = Label(self.root, text = "Pick an animal")
        self.animal_lbl.grid(row = 7, column = 0, sticky = "ew", padx = 10)

        self.combo_box = ttk.Combobox(self.root, state="readonly", values=["Unicorn", "Spider", "Bat"])
        self.combo_box.grid(row = 8, column = 0, sticky = "ew", padx = 10)

        self.animal = self.combo_box.get()

        self.print_btn = Button(self.root, text = "Go!", command = self.generate_name)
        self.print_btn.grid(row = 9, column = 0, sticky = "ew", padx = 10)

        self.output_lbl = Label(self.root, text = "",)
        self.output_lbl.grid(row = 10, column = 0, sticky = "ew", padx = 10, pady=10)

    def generate_name(self):
        self.output_lbl.config(text = f"You are the {self.selected_var} {self.box.get()} {self.combo_box.get()}!")






root = Tk()
run = Generator(root)
root.mainloop()