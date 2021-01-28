from tkinter import *

root = Tk()
root.title('Zaagcalculator')

def myClick():
    myLabel = Label(
        root,
        text="Inderdaad ik ben een knop."
    )
    myLabel.pack()

myButton = Button(
    root,
    text="Ik ben een knop",
    command=myClick,
    fg="white",
    bg="black"
)
myButton.pack()

root.mainloop()