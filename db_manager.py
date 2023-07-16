import sqlite3

class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite")

    def getConnection(self):
        return self.conn

    def closeConnection(self):
        self.conn.close()
    
    

