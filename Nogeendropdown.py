import tkinter as tk
import sqlite3 as sq
import datetime


# Connection to SQLite
con = sq.connect('Cars.db')

# Car choice dictionary for drop-down menu
carD = ['BMW', 'Volvo', 'Mitsubishi']


root = tk.Tk()
canvas = tk.Canvas(root, height=500, width= 500, bg="white")
canvas.pack()

carV = tk.StringVar(root)
carV.set('Choose your car')

carDDM = tk.OptionMenu(canvas, carV, *carD)
carDDM.pack()

# Function for inserting car choice from drop-down menu into SQLite
def SaveCarChoice():
    c = con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS CAR (sql_date VARCHAR(20), sql_carV VARCHAR(20) NOT NULL)')
    today = str(datetime.date.today())
    today = today[8:] + '-' + today[5:7] + '-' + today[:4]
    c.execute('INSERT INTO CAR (sql_date, sql_carV) VALUES (?, ?)', (today, carV.get()))
    con.commit()

# Button for user to activate the function inserting data into SQLite
carB = tk.Button(canvas, text="Enter", command=SaveCarChoice)
carB.pack()

root.mainloop()