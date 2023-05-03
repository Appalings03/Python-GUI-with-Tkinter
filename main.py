from tkinter import *
import tkinter as tk

class MyApp:

    def __init__(self, root):
        root.title("My app")

        root.geometry("500x400")
        root.maxsize(1000,800)
        self.initUI(root)
    
    def initUI(self,root):
        self.label_text = StringVar()
        label = Label(root, text="Some label text", textvariable=self.label_text)
        #label.pack(side=tk.LEFT, padx=10, pady=5)
        label.grid(column=1,row=1)

        #label["text"] = "New Label text"
        #label["font"] = ("Courier", 40)

        label.configure(text="New label",font=("Courier", 40))

        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        #entry.pack(side=tk.LEFT)
        #entry.place(x=100, y=50)
        entry.grid(column=2, row=1)

        #label["textvariable"] = entry_text

        button = Button(root, text="Button text", command=self.press_button)
        #button.pack(side=tk.LEFT)
        button.grid(column=1, row=2, sticky=(S,E,W))
        
        self.list_item_strings = ["Hey", "Hi", "Hello", "Bonjour", "Yo"]
        list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(root, listvariable=list_items)
        #listbox.pack(side=tk.LEFT, padx=10, pady=5)
        listbox.grid(column=2, row=2)
        listbox["height"] = 3
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_items(listbox.curselection()))
    
    def press_button(self):
        print("Button Press")
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_items(self, index):
        selected_item = self.list_item_strings[index[0]]
        print(selected_item)
    

root =Tk()

MyApp(root)

root.mainloop()