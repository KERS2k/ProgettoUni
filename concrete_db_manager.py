from db_manager import DbManager

class ConcreteDbManager(DbManager):
    def getConnection(self):
        return self.conn

    def closeConnection(self):
        self.conn.close()