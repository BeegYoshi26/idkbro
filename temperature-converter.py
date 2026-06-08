from tkinter import *

AB_ZERO_C = -273.15
AB_ZERO_F = -495.67

FONT_MAIN_TITLE = "Verdana 16 bold"
FONT_HEADER = "Verdana 12 bold"
FONT_DEFAULT = "Verdana 12"

class TemperatureConverter:
    
    def convertCtoF(self, temp):
        try:
            temp = float(temp)
            if temp >= AB_ZERO_F:
                result = (float(temp) * 9/5) + 32
                return f"{result:.1f} degrees centigrade"
            else:
                return "Temperature is too low"
        except ValueError:
            return "Enter a valid temperature"
        
    def convertFtoC(self, temp):
        try:
            temp = float(temp)
            if temp >= AB_ZERO_C:
                result = (float(temp) - 32) * 5/9
                return f"{result:.1f} degrees farenheight"
            else:
                return "Temperature is too low"     
        except ValueError:
            return "Enter a valid temperature"

class ConverterGUI:

    def __init__(self, root):

        self.converter = TemperatureConverter()

        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x150")

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.frames = ()

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_fFrame"] = self.create_to_fFrame()
        self.frames["to_cFrame"] = self.create_to_cFrame()

        self.show_frame("MainFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
