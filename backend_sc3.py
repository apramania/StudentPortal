import sqlite3

def connect():
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name text,enrollment text,roll text,contact integer)")
    conn.commit()
    conn.close()

def insert(name,enrollment,roll,contact):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?)",(name,enrollment,roll,contact))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(name = "",enrollment = "",roll = "",contact = ""):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR enrollment = ? OR roll = ? OR contact = ?",(name,enrollment,roll,contact))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update(id,name,enrollment,roll,contact):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=?,enrollment=?,roll=?,contact=? WHERE id=?",(name,enrollment,roll,contact,id))
    conn.commit()
    conn.close()

connect()
#insert("Jack","AU/2017/3012","UG/02/36",764684554)
#insert("Jack","AU/2017/3012","UG/02/36",764684554)
#update(2,"Appy","AU/2017/3012","UG/02/36",764684554)
#print(view())
#delete(2)
#print(view())

#print(search(name="Appy"))


