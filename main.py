from tkinter import *


class MyApp:

    def __init__(self, root):
        root.title("My app")

        root.geometry("500x400")
        root.maxsize(1000,800)
        self.initUI(root)
    
    def initUI(self,root):
        label = Label(root, text="Some label text")
        label.pack()

root =Tk()

MyApp(root)

root.mainloop()