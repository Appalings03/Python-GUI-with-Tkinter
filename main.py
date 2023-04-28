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

        #label["text"] = "New Label text"
        #label["font"] = ("Courier", 40)

        label.configure(text="New label",font=("Courier", 40))

root =Tk()

MyApp(root)

root.mainloop()