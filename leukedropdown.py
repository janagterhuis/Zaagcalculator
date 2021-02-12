from tkinter import *
import sqlite3

# Create a database
conn = sqlite3.connect('prijzenlijst.db')

# Create cursor
c = conn.cursor()

def option_changed(*args):
    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()
    soort = format(variable.get())

    c.execute("SELECT dikte FROM plaatmateriaal WHERE soort = 'Multiplex'")

    global dikte_record
    dikte_record = list(c.fetchall())

    print (dikte_record)
    print (soort)

    opties = (dikte_record)

    diktes = StringVar(master)
    diktes.set("diktes")  # default value

    m = OptionMenu(master, diktes, *opties)
    m.pack()

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

master = Tk()

c.execute("SELECT soort FROM plaatmateriaal")
global soort_record
soort_record = set(c.fetchall())

options = soort_record

a = "Foo"
variable = StringVar(master)
variable.set("soorten") # default value
variable.trace("w", option_changed)

w = OptionMenu(master, variable, *options)
w.pack()

# Commit changes
conn.commit()

# Close connection
conn.close()

mainloop()