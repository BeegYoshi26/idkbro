from tkinter import *

class FrameExample:

    def __init__(self, root):
        self.root = root
        self.root.title("Sidebar Using Frames")

        # configure the grid structure
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, minsize=100)
        self.root.columnconfigure(1, weight=1)

        # run widgets function
        self.create_widgets()

    def create_widgets(self):

        # create sidebar frame
        self.sidebar_frame = Frame(self.root, bg="#333333")
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")

        # create buttons inside the sidebar
        self.btn1 = Button(self.sidebar_frame, text="Dashboard")
        self.btn1.pack(pady=10, padx=10, fill=X)

        self.btn2 = Button(self.sidebar_frame, text="Settings")
        self.btn2.pack(pady=10, padx=10, fill=X)

        # create main content frame
        self.content_frame = Frame(self.root, bg="white")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # create label  inside the main content frame
        self.intro_label = Label(self.content_frame, text="Welcome!", bg="white", font = ("Verdana 24"))
        self.intro_label.pack(expand=True)

root = Tk()
run = FrameExample(root)
root.mainloop()