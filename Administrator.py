from tkinter import *
import sqlite3

root = Tk()
root.title('Administrator pagina')

# Database

# Create a database
conn = sqlite3.connect('prijzenlijst.db')

# Create cursor
c = conn.cursor()

# Create table
'''c.execute("""CREATE TABLE plaatmateriaal(
        breedte integer,
        lengte integer,
        dikte integer,
        soort text,
        prijs integer)""")'''

# Create Edit function to update a record
def update():
    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE plaatmateriaal SET
        breedte = :breedte,
        lengte = :lengte,
        dikte = :dikte,
        soort = :soort,
        prijs = :prijs

        WHERE oid = :oid""" ,
              {
                  'breedte': breedte_editor.get(),
                  'lengte': lengte_editor.get(),
                  'dikte': dikte_editor.get(),
                  'soort': soort_editor.get(),
                  'prijs': prijs_editor.get(),

                  'oid': record_id
              }
              )

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title('editor')

    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query database
    c.execute("SELECT * FROM plaatmateriaal WHERE oid = " + record_id)
    records = c.fetchall()

    # Create Global variables
    global breedte_editor
    global lengte_editor
    global dikte_editor
    global soort_editor
    global prijs_editor

    # Create text boxes
    breedte_editor = Entry(editor, width=30)
    breedte_editor.grid(row=0, column=1, padx=20)
    lengte_editor = Entry(editor, width=30)
    lengte_editor.grid(row=1, column=1)
    dikte_editor = Entry(editor, width=30)
    dikte_editor.grid(row=2, column=1)
    soort_editor = Entry(editor, width=30)
    soort_editor.grid(row=3, column=1)
    prijs_editor = Entry(editor, width=30)
    prijs_editor.grid(row=4, column=1)

    # Create text box labels
    breedte_label = Label(editor, text="Breedt (cm)")
    breedte_label.grid(row=0, column=0)
    lengte_label = Label(editor, text="Lengte (cm)")
    lengte_label.grid(row=1, column=0)
    dikte_label = Label(editor, text="Dikte (mm)")
    dikte_label.grid(row=2, column=0)
    soort_label = Label(editor, text="Soort")
    soort_label.grid(row=3, column=0)
    prijs_label = Label(editor, text="Prijs")
    prijs_label.grid(row=4, column=0)

    # Loop through results
    for record in records:
        breedte_editor.insert(0, record[0])
        lengte_editor.insert(0, record[1])
        dikte_editor.insert(0, record[2])
        soort_editor.insert(0, record[3])
        prijs_editor.insert(0, record[4])

    # Create a save button
    save_btn = Button(editor, text="Save record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


# Create function to delete a record
def delete():
    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()

    # Delete records
    c.execute("DELETE from plaatmateriaal WHERE oid= " + delete_box.get())

    delete_box.delete(0, END)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create submit function for database
def submit():
    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO plaatmateriaal VALUES(:breedte, :lengte, :dikte, :soort, :prijs)",
              {
                  'breedte': breedte.get(),
                  'lengte': lengte.get(),
                  'dikte': dikte.get(),
                  'soort': soort.get(),
                  'prijs': prijs.get(),
              })

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Clear the text boxes
    breedte.delete(0, END)
    lengte.delete(0, END)
    dikte.delete(0, END)
    soort.delete(0, END)
    prijs.delete(0, END)

# Create query function
def query():
    # Create a database
    conn = sqlite3.connect('prijzenlijst.db')

    # Create cursor
    c = conn.cursor()

    # Query database
    c.execute("SELECT *, oid FROM plaatmateriaal")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Create text boxes
breedte = Entry(root, width=30)
breedte.grid(row=0, column=1, padx=20)
lengte = Entry(root, width=30)
lengte.grid(row=1, column=1)
dikte = Entry(root, width=30)
dikte.grid(row=2, column=1)
soort = Entry(root, width=30)
soort.grid(row=3, column=1)
prijs = Entry(root, width=30)
prijs.grid(row=4, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
breedte_label = Label(root, text="Breedte (cm)")
breedte_label.grid(row=0, column=0)
lengte_label = Label(root, text="Lengte (cm)")
lengte_label.grid(row=1, column=0)
dikte_label = Label(root, text="Dikte (mm)")
dikte_label.grid(row=2, column=0)
soort_label = Label(root, text="Soort")
soort_label.grid(row=3, column=0)
prijs_label = Label(root, text="Prijs")
prijs_label.grid(row=4, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create subit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

# Create a Queary button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create a Delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create an Update button
edit_btn = Button(root, text="Edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()