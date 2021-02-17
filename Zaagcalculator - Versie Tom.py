from tkinter import *
import sqlite3

root = Tk()
root.title('Zaagcalculator')
# Create a database


breedte = Entry(
    root,
    width=20
)
lengte = Entry(
    root,
    width=20
)
breedte.grid(column = 1, row=1, padx=10, pady=10, columnspan=2)
lengte.grid(column=3, row = 1,  padx=10, pady=10, columnspan=2)
breedte.insert(0, "breedte ")
lengte.insert(0, "lengte")

def update_options(*args):
    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()
    c.execute("SELECT dikte FROM plaatmateriaal WHERE soort = (?)", (clicked_soorten,))
    print(clicked_soort.get())
    # (?)", (clicked_soort)
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

def bereken():
    parameter1 = int(breedte.get())
    parameter2 = int(lengte.get())
    berekening = parameter1 * parameter2
    uitkomst = "De uitkomst is: " + str(berekening)
    antwoord = Label(
        root,
        text= uitkomst
    )
    antwoord.grid(column=1, row=2)

bereken = Button(root,
    text="Berekenen",
    command=bereken,
    fg="white",
    bg="grey"
)
bereken.grid(column=7, row=1, padx=30, pady=5, columnspan=2)



# Create a database
conn = sqlite3.connect('prijzenlijst.db')

# Create cursor
c = conn.cursor()

c.execute("SELECT soort FROM plaatmateriaal")
global soort_record
soort_record = list(set(c.fetchall()))
print(soort_record)

soorten = soort_record

clicked_soort = StringVar()
clicked_soorten = clicked_soort.get()
if clicked_soort.get == '' :
    clicked_soorten = ('MDF',)
else:
    clicked_soorten = clicked_soort.get()

clicked_soort.set(soorten[0])
clicked_soort.trace('w', update_options)

print(clicked_soort)

drop = OptionMenu(root, clicked_soort, *soorten)
drop.grid(column=5, row=1, columnspan=1)

c.execute("SELECT dikte FROM plaatmateriaal WHERE soort = (?)", (clicked_soorten,))
global dikte_record
dikte_record = list(set(c.fetchall()))
print(dikte_record)
print (sorted(dikte_record, key=str, reverse=True))


diktes = dikte_record
clicked_dikte = StringVar()
clicked_dikte.set(18)

drop = OptionMenu(root, clicked_dikte, *diktes)
drop.grid(column=6, row=1, columnspan=1)

# Commit changes
conn.commit()

# Close connection
conn.close()




root.mainloop()