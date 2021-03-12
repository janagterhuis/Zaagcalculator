from tkinter import *
import sqlite3

root = Tk()
root.title('Zaagcalculator')

# Invoervelden definiëren
breedte = Entry(root,width=20)
lengte = Entry(root,width=20)
aantal = Entry(root,width=20)

# Invoervelden plaatsen
breedte.grid(column = 1, row=1, padx=10, pady=10, columnspan=2)
lengte.grid(column=3, row = 1,  padx=10, pady=10, columnspan=2)
aantal.grid(column = 5, row=1, padx=10, pady=10, columnspan=1)

# Invoervelden verbreden
breedte.insert(0, "breedte ")
lengte.insert(0, "lengte")
aantal.insert(0, "aantal ")

# Functies
def selected_soort(soort):
    selected_soort.s = soort

    # Database openen
    conn = sqlite3.connect('prijzenlijst.db')

    # Cursor maken
    c = conn.cursor()

    # Alle diktes ophalen van gekozen soort
    c.execute("SELECT dikte FROM plaatmateriaal WHERE soort = ?", (selected_soort.s))
    # Diktes in een lijst zetten
    dikte_record = list(set(c.fetchall()))

    # Standaard waarde geven
    clicked_dikte = StringVar()
    clicked_dikte.set("dikte")

    # Drop down menu definiëren
    drop = OptionMenu(root, clicked_dikte, *dikte_record, command=selected_dikte)

    # Drop down menu plaatsen
    drop.grid(column=7, row=1, columnspan=1)

    # Drop down menu verbreden
    drop.config(width =5)

    # Veranderingen opslaan
    conn.commit()

    # Connectie verbreken
    conn.close()

def selected_dikte(dikte):
    # Gekozen dikte definiëren
    selected_dikte.d = dikte

def bereken():
    # Antwoord definiëren
    antwoord = Label(root,)
    # Oude Antwoord verwijderen
    antwoord.destroy()

    # Database openen
    conn = sqlite3.connect('prijzenlijst.db')

    # Cursor maken
    c = conn.cursor()

    # De plaatprijs ophalen van de gekozen soort en dikte
    c.execute("SELECT prijs FROM plaatmateriaal WHERE soort = ? AND dikte = ?", (selected_soort.s[0], selected_dikte.d[0]))
    # De output definiëren
    prijs_record = c.fetchone()

    # Veranderingen opslaan
    conn.commit()

    # Connectie verbreken
    conn.close()

    # Ingevoer ophalen
    parameter1 = float(int(breedte.get()))
    parameter2 = float(int(lengte.get()))
    parameter3 = float(int(aantal.get()))

    # Database openen
    conn = sqlite3.connect('prijzenlijst.db')

    # Cursor maken
    c = conn.cursor()

    # Breedte van de gekozen plaat ophalen
    c.execute("SELECT breedte FROM plaatmateriaal WHERE prijs = ?", (prijs_record))
    breedte_record = c.fetchone()
    # Lengte van de gekozen plaat ophalen
    c.execute("SELECT lengte FROM plaatmateriaal WHERE prijs = ?", (prijs_record))
    lengte_record = c.fetchone()

    # Vierkante centimeter prijs berekenen
    vierkante_cm_prijs = (int(prijs_record[0])/(int(breedte_record[0]) * int(lengte_record[0])))

    # Veranderingen opslaan
    conn.commit()

    # Connectie verbreken
    conn.close()

    # Berekening definiëren
    berekening = (1.3 * vierkante_cm_prijs * parameter1 * parameter2 * parameter3)
    # Prijs definiëren
    uitkomst = "De prijs is: €" + str(("%.2f" % round( berekening,2)))
    antwoord = Label(root,text= uitkomst)
    # Prijs plaatsen
    antwoord.grid(column=1, row=2)

def administrator():
    # Nieuw venster maken
    administrator = Tk()
    # Titel van het nieuwe venster
    administrator.title('Administrator pagina')

    # Database openen
    conn = sqlite3.connect('prijzenlijst.db')

    # Cursor maken
    c = conn.cursor()

    # Tabel maken
    '''c.execute("""CREATE TABLE plaatmateriaal(
            breedte integer,
            lengte integer,
            dikte integer,
            soort text,
            prijs integer)""")'''

    # Functie voor het updaten van records
    def update():
        # Database openen
        conn = sqlite3.connect('prijzenlijst.db')

        # Cursor maken
        c = conn.cursor()

        # Velden leeg maken
        record_id = delete_box.get()

        # Velden koppelen aan de database
        c.execute("""UPDATE plaatmateriaal SET
            breedte = :breedte,
            lengte = :lengte,
            dikte = :dikte,
            soort = :soort,
            prijs = :prijs
            WHERE oid = :oid""",
                  {
                      'breedte': breedte_editor.get(),
                      'lengte': lengte_editor.get(),
                      'dikte': dikte_editor.get(),
                      'soort': soort_editor.get(),
                      'prijs': prijs_editor.get(),
                      'oid': record_id
                  }
                  )

        # Veranderingen opslaan
        conn.commit()

        # Connectie verbreken
        conn.close()

        editor.destroy()
    # Records veranderen
    def edit():
        global editor
        editor = Tk()
        editor.title('editor')

        # Database openen
        conn = sqlite3.connect('prijzenlijst.db')

        # Cursor maken
        c = conn.cursor()

        record_id = delete_box.get()
        # Alle records in de velden invullen
        c.execute("SELECT * FROM plaatmateriaal WHERE oid = " + record_id)
        records = c.fetchall()

        # Variabels global maken
        global breedte_editor
        global lengte_editor
        global dikte_editor
        global soort_editor
        global prijs_editor

        # Invoervelden definiëren
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

        # Invoervelden maken
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

        # Resultaten bekijken
        for record in records:
            breedte_editor.insert(0, record[0])
            lengte_editor.insert(0, record[1])
            dikte_editor.insert(0, record[2])
            soort_editor.insert(0, record[3])
            prijs_editor.insert(0, record[4])

        # Save button maken
        save_btn = Button(editor, text="Save record", command=update)
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Functie voor het verwijderen van records
    def delete():
        # Open database
        conn = sqlite3.connect('prijzenlijst.db')

        # Cursor maken
        c = conn.cursor()

        # Record verwijderen
        c.execute("DELETE from plaatmateriaal WHERE oid= " + delete_box.get())
        delete_box.delete(0, END)

        # Veranderingen opslaan
        conn.commit()

        # Connectie verbreken
        conn.close()

    def submit():
        # Database openen
        conn = sqlite3.connect('prijzenlijst.db')

        # Cursor maken
        c = conn.cursor()

        # Invoeren in tabel
        c.execute("INSERT INTO plaatmateriaal VALUES(:breedte, :lengte, :dikte, :soort, :prijs)",
                  {
                      'breedte': breedte.get(),
                      'lengte': lengte.get(),
                      'dikte': dikte.get(),
                      'soort': soort.get(),
                      'prijs': prijs.get(),
                  })

        # Veranderingen opslaan
        conn.commit()

        # Connectie verbreken
        conn.close()

        # Invoervelden leeg maken
        breedte.delete(0, END)
        lengte.delete(0, END)
        dikte.delete(0, END)
        soort.delete(0, END)
        prijs.delete(0, END)

    # Query functie maken
    def query():
        # Database openen
        conn = sqlite3.connect('prijzenlijst.db')

        # Cursor maken
        c = conn.cursor()

        # Query database
        c.execute("SELECT *, oid FROM plaatmateriaal")
        records = c.fetchall()


        print_records = ''

        # Door de resultaten gaan
        for record in records:
            print_records += str(record) + "\n"
        query_label = Label(administrator, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

        # Veranderingen opslaan
        conn.commit()

        # Connectie verbreken
        conn.close()

    # Invoervelden definiëren
    breedte = Entry(administrator, width=30)
    breedte.grid(row=0, column=1, padx=20)
    lengte = Entry(administrator, width=30)
    lengte.grid(row=1, column=1)
    dikte = Entry(administrator, width=30)
    dikte.grid(row=2, column=1)
    soort = Entry(administrator, width=30)
    soort.grid(row=3, column=1)
    prijs = Entry(administrator, width=30)
    prijs.grid(row=4, column=1)

    delete_box = Entry(administrator, width=30)
    delete_box.grid(row=9, column=1, pady=5)

    # Invoervelden maken
    breedte_label = Label(administrator, text="Breedte (cm)")
    breedte_label.grid(row=0, column=0)
    lengte_label = Label(administrator, text="Lengte (cm)")
    lengte_label.grid(row=1, column=0)
    dikte_label = Label(administrator, text="Dikte (mm)")
    dikte_label.grid(row=2, column=0)
    soort_label = Label(administrator, text="Soort")
    soort_label.grid(row=3, column=0)
    prijs_label = Label(administrator, text="Prijs")
    prijs_label.grid(row=4, column=0)

    delete_box_label = Label(administrator, text="Select ID")
    delete_box_label.grid(row=9, column=0, pady=5)

    # Submit konp maken
    submit_btn = Button(administrator, text="Add record to database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

    # Query knop maken
    query_btn = Button(administrator, text="Show records", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

    # Delete knop maken
    delete_btn = Button(administrator, text="Delete record", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Update knop maken
    edit_btn = Button(administrator, text="Edit record", command=edit)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=142)

    # Veranderingen opslaan
    conn.commit()

    # Connectie verbreken
    conn.close()

# Bereken knop maken
bereken = Button(root,text="Berekenen",command=bereken,fg="white",bg="grey")
bereken.grid(column=8, row=1, padx=5, pady=10, columnspan=2)
bereken.config(width=12)

# Administrator knop maken
administrator = Button(root,text="administrator",command=administrator,fg="white",bg="grey")
administrator.grid(column=8, row=2, padx=10, pady=5, columnspan=2)
administrator.config(width=12)

# Database openen
conn = sqlite3.connect('prijzenlijst.db')

# Cursor maken
c = conn.cursor()

# Alle soorten uit de database ophalen
c.execute("SELECT soort FROM plaatmateriaal")
# De resulaten in een lijst zetten
soort_record = list(set(c.fetchall()))

# Standaard waarde geven
clicked_soort = StringVar()
clicked_soort.set("soort")

# Dropdown menu maken
drop = OptionMenu(root, clicked_soort, *soort_record, command=selected_soort )
drop.grid(column=6, row=1, columnspan=1)
drop.config(width =9)

# Veranderingen opslaan
conn.commit()

# Connectie verbreken
conn.close()

root.mainloop()