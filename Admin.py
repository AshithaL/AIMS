from sqlite3 import Error
import sqlite3
from pprint import pprint
#from Credentials import credentials
from datetime import date

def funct():
    """
    Using a dictionary to Call a particular method.
    Calls the function using the user-input.
    """
    option = {
        "1": ("Create Member Profile", createMp),
        "2": ("Insert Member Profile", insertMp),
        "3": ("Update Member Profile", updateMp),
        "4": ("Delete Member Profile", deleteMp),
        "5": ("Create Supervising Team", createSt),
        "6": ("Insert Supervising Team", insertSt),
        "7": ("Delete Supervising Team", deleteSt),
        "8": ("Update Supervising Team", updateSt)
    }

    ans = input("Choose:\n"
                    "1.Create Member Profile.\n"
                    "2.Insert Member Profile.\n"
                    "3.Update Member Profile.\n"
                    "4.Delete Member Profile.\n"
                    "5.Create Supervising Team.\n"
                    "6.Insert Supervising Team.\n"
                    "7.Delete Supervising Team.\n"
                    "8.Update Supervising Team.\n")

    option.get(ans)[1](con)

def sqlConn():
    """A function used in connecting to database"""
    try:
        con = sqlite3.connect('aims.db')
        print("Connection established: Database is created")
        return con
    except Error:
        print(Error)

def login():
    """A login function"""
    password = 1111
    enteredPassword = int(input("Enter password"))
    if enteredPassword == password:
        print("Success")
        funct()
    else:
        print("Try again")

def createMp(con):
    cursorObj = con.cursor()
    a = str(input("Enter table name to create"))
    cursorObj.execute('Create table if not exists {} (Id integer PRIMARY KEY, Name text, Address text)'.format(a))
    con.commit()

def insertMp(con):
    cursor = con.cursor()
    tablename = str(input("Enter table name"))
    id = int(input("Enter id:\n"))
    name = str(input("Name:\n"))
    add = str(input("Address:\n"))
    cursor.execute('Insert into '+ tablename +' (Id ,Name, Address) values (?, ?, ?)', (id, name, add))
    con.commit()

def updateMp(con):
    cursor = con.cursor()
    cursor.execute('Update Member_profile Set Name = "Brians" where Id = 2')
    cursor.fetchall()
    print("Updated successfully")
    con.commit()

def deleteMp(con):
    cursor = con.cursor()
    data = input("Enter the Id:")
    cursor.execute('Delete from Member_profile where Id=?', (data, ))
    con.commit()

def createSt(con):
    cursor = con.cursor()
    ans = str(input("Enter Supervising team name-"))
    cursor.execute('Create table if not exists {} (tid integer PRIMARY KEY, m_name text, m_id)'.format(ans))
    con.commit()

def insertSt(con):
    cursor = con.cursor()
    tablename = input("Enter Supervising Team name-")
    pid = int(input("Enter Team Id-\n"))
    name = str(input("Enter Member name-\n"))
    mid = str(input("Emter Member id-\n"))

    cursor.execute('Insert into '+ tablename +' (tid, m_name, m_id) values (?, ?, ?)',
                   (pid, name, mid))
    con.commit()

def deleteSt(con):
    cursor = con.cursor()
    ans = input("Enter STeam Id-")
    cursor.execute('Delete from STeam where tid=?', (ans, ))
    con.commit()

def updateSt(con):
    cursor = con.cursor()
    cursor.execute('Update STeam Set m_name = "Rachel" where tid = 101 ')
    con.commit()

# def assign(con):
#     cursor = con.cursor()
#     cursor.execute('')
#     con.commit()

# def judgement(con):
#     cursor = con.cursor()
#     cursor.execute('')
#     con.commit()

con = sqlConn()
login()