from tkinter import *
import tkinter as tk

class ToDoItem:

    def __init__(self, name, description):
        self.name = name
        self.description = description



class ToDoListApp:

    def __init__(self, root):
        root.title("TO DO List")
        self.to_do_items = [
            ToDoItem("Workout", "Push ups, pull ups, squats"),
            ToDoItem("House work", "Clean Kitchen, sweep floor, do laundry"),
            ToDoItem("Groceries", "Buy bread, milk, eggs")
        ]
        self.initUI(root)
        
    
    def initUI(self,root):
        frame = Frame(root, borderwidth=2, relief="sunken")
        frame.grid(column=1,row=1, sticky=(N, E, S,W))
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        list_label = Label(frame, text="To Do Items")
        list_label.grid(column=1, row=1, sticky=(S, W))

        self.to_do_names = StringVar(value=list(map(lambda x: x.name, self.to_do_items)))

        #self.list_item_strings = ["Hey", "Hi", "Hello", "Bonjour", "Yo"]
        #list_items = StringVar(value=self.list_item_strings)
        list_items = Listbox(frame, listvariable=self.to_do_names)
        #listbox.pack(side=tk.LEFT, padx=10, pady=5)
        #listbox["height"] = 3
        list_items.bind("<<ListboxSelect>>", lambda s: self.select_items(list_items.curselection()))
        list_items.grid(column=1, row=2, sticky=(E, W))

        self.selected_description = StringVar()

        selected_description_label = Label(frame, textvariable=self.selected_description)
        selected_description_label.grid(column=1, row=3, sticky=(E, W))


        '''self.label_text = StringVar()
        label = Label(frame, text="Some label text", textvariable=self.label_text)
        #label.pack(side=tk.LEFT, padx=10, pady=5)
        #label.grid(column=1,row=1)

        #label["text"] = "New Label text"
        #label["font"] = ("Courier", 40)

        label.configure(text="New label",font=("Courier", 40))

        self.entry_text = StringVar()
        entry = Entry(frame, textvariable=self.entry_text)
        #entry.pack(side=tk.LEFT)
        #entry.place(x=100, y=50)
        #entry.grid(column=2, row=1)

        #label["textvariable"] = entry_text

        button = Button(frame, text="Button text", command=self.press_button)
        #button.pack(side=tk.LEFT)
        #button.place(x=0,y=0)
        #button.configure(width=10, height=20, font=("Courier", 40))
        #button.grid(column=1, row=2, sticky=(S,E,W))'''
        
        
    def press_button(self):
        print("Button Press")
        text = self.entry_text.get()
        self.label_text.set(text)

    def select_items(self, index):
        selected_item = self.to_do_items[index[0]]
        self.selected_description.set(selected_item.description)
    

root =Tk()

ToDoListApp(root)

root.mainloop()