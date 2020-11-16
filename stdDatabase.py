import sqlite3


def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student (oid INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, DoB text,
                    Age text, Gender text, Address text, Mobile text)""")
    con.commit()
    con.close()


def addStdRec( StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    studentData()
    cur.execute("INSERT INTO student (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile) VALUES (?,?,?,?,?,?,?,?)",
                 (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(oid):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE from student WHERE oid=?", (oid,))
    con.commit()
    con.close()


def searchData(StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=?, OR Firstname=?, OR Surname=?, OR DoB=?, OR Age=?, OR Gender=?, OR Address=?, OR Mobile=?" , (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate( StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE student SET  StdID=?,Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?",
        (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile,))
    con.commit()
    con.close()
