from tkinter import *

root = Tk()
root.title('Zaagcalculator')

#Creating the widgets
myLabel = Label(root, text="Hello world!")
myLabel1 = Label(root, text="Hallo wereld")

#Showing the widgets
myLabel.grid(row="0", column="0")
myLabel1.grid(row="1", column="1")

root.mainloop()