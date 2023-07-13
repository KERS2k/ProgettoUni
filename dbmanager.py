import sqlite3

class Dbmanager:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite")

    def closeConnection(self):
        self.conn.close()
    
    def getConnection(self):
        return self.conn
    

