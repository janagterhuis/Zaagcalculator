from tkinter import *

root = Tk()
root.title('Zaagcalculator')

# Drop Down Boxes

def show():
    myLabel=Label(root, text=clicked.get()).pack()

options = [
    "Multiplex",
    "MDF",
    "Spaanplaat",
    "Plexiglas"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()