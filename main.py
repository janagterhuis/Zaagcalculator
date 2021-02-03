from tkinter import *

root = Tk()
root.title('Zaagcalculator')

myEntry = Entry(
    root,
    width=50
)
myEntry.pack()
myEntry.insert(0, "Geef je naam: ")
def myClick():
    Hallo = "Hallo ik heet " + myEntry.get()
    myLabel = Label(
        root,
        text=Hallo
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