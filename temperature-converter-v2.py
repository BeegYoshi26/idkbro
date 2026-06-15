from tkinter import *

AB_ZERO_C = -273.15
AB_ZERO_F = -459.67

FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADER = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

class TemperatureConverter:
    
    def convertCtoF(self, temp):
        try:
            temp = float(temp)
            if temp >= AB_ZERO_F:
                # calculates calsius to fahrenheit
                result = (float(temp) * 9/5) + 32

                return f"{result:.1f} degrees fahrenheit"
            else:
                return "Temperature is too low"
        except ValueError or "":
            return "Enter a valid temperature"
        
    def convertFtoC(self, temp):
        try:
            temp = float(temp)
            if temp >= AB_ZERO_C:
                # calculates fahrenheit to celsius
                result = (float(temp) - 32) * 5/9

                return f"{result:.1f} degrees centigrade"
            else:
                return "Temperature is too low"     
        except ValueError or "":
            return "Enter a valid temperature"

class ConverterGUI:

    def __init__(self, root):

        self.converter = TemperatureConverter()

        # main window
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x150")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # container for frames
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        # dictionary to hold frames
        # key is the frame name and value is the method that creates the frame
        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_fFrame"] = self.create_to_fFrame()
        self.frames["to_cFrame"] = self.create_to_cFrame()

        # show the initial frame
        self.show_frame("MainFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise() # moves the frame to the top of the stack

    def create_main_frame(self):

        MainFrame = Frame(self.container)
        MainFrame.grid(row=0, column=0, sticky="nsew")

        MainFrame.rowconfigure([0,1], weight=1)
        MainFrame.columnconfigure([0,1], weight=1)

        Label(MainFrame, text="Temperature Converter", font=FONT_MAIN_TITLE).grid(row=0, columnspan=2, sticky="nsew")
        
        Button(MainFrame, text="to Centigrade", bg="yellow", font=FONT_HEADER, command=lambda:self.show_frame("to_cFrame")).grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        Button(MainFrame, text="to Fahrenheit", bg="pink", font=FONT_HEADER, command=lambda:self.show_frame("to_fFrame")).grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        return MainFrame

    def create_to_cFrame(self):
        to_cFrame = Frame(self.container)
        to_cFrame.grid(row=0, column=0, sticky="nsew")

        to_cFrame.rowconfigure([0,1,2,3], weight=1)
        to_cFrame.columnconfigure([0,1,2], weight=1)

        Label(to_cFrame, justify=CENTER, text="Enter the temp in Fahrenheit", font=FONT_HEADER).grid(row=0, columnspan=3, sticky="nsew", padx=10)

        self.temp_entry_c = Entry(to_cFrame, justify=CENTER, font=FONT_DEFAULT)
        self.temp_entry_c.grid(row=1, columnspan=3, sticky="nsew", padx=10, pady=10)

        calculate = Button(to_cFrame, text="Calculate", font=FONT_DEFAULT, command=lambda:self.to_centigrade())
        calculate.grid(row=2, column=0, sticky="nsew")

        reset = Button(to_cFrame, text="Reset", font=FONT_DEFAULT, command=lambda:self.reset_to_cFrame())
        reset.grid(row=2, column=1, sticky="nsew")

        back = Button(to_cFrame, text="Back", font=FONT_DEFAULT, command=lambda:self.show_frame("MainFrame"))
        back.grid(row=2, column=2, sticky="nsew")

        self.result_c = Label(to_cFrame, text="Please enter a number", font=FONT_DEFAULT)
        self.result_c.grid(row=3, columnspan=3, sticky="nsew", padx=10)

        return to_cFrame
    
    def to_centigrade(self):
        data = self.temp_entry_c.get()
        converted_result = self.converter.convertFtoC(data)
        self.result_c.config(text=converted_result)

    def reset_to_cFrame(self):
        self.temp_entry_c.delete(0, END)
        self.result_c.config(text="Please enter a number")


    def create_to_fFrame(self):

        to_fFrame = Frame(self.container)
        to_fFrame.grid(row=0, column=0, sticky="nsew")

        to_fFrame.rowconfigure([0,1,2,3], weight=1)
        to_fFrame.columnconfigure([0,1,2], weight=1)

        Label(to_fFrame, justify=CENTER, text="Enter the temp in Centigrade", font=FONT_HEADER).grid(row=0, columnspan=3, sticky="nsew", padx=10)

        self.temp_entry_f = Entry(to_fFrame, justify=CENTER, font=FONT_DEFAULT)
        self.temp_entry_f.grid(row=1, columnspan=3, sticky="nsew", padx=10, pady=10)

        calculate = Button(to_fFrame, text="Calculate", font=FONT_DEFAULT, command=lambda:self.to_fahrenheit())
        calculate.grid(row=2, column=0, sticky="nsew")

        reset = Button(to_fFrame, text="Reset", font=FONT_DEFAULT, command=lambda:self.reset_to_fFrame())
        reset.grid(row=2, column=1, sticky="nsew")

        back = Button(to_fFrame, text="Back", font=FONT_DEFAULT, command=lambda:self.show_frame("MainFrame"))
        back.grid(row=2, column=2, sticky="nsew")

        self.result_f = Label(to_fFrame, text="Please enter a number", font=FONT_DEFAULT)
        self.result_f.grid(row=3, columnspan=3, sticky="nsew", padx=10)

        return to_fFrame
    
    def to_fahrenheit(self):
        data = self.temp_entry_f.get()
        converted_result = self.converter.convertCtoF(data)
        self.result_f.config(text=converted_result)

    def reset_to_fFrame(self):
        self.temp_entry_f.delete(0, END)
        self.result_f.config(text="Please enter a number")

root = Tk()
run = ConverterGUI(root)
root.mainloop()