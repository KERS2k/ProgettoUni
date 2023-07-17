import abc
import sqlite3

class DbManager(abc.ABC):

    def __init__(self):
        # Costruttore della classe DbManager
        self.conn = sqlite3.connect("database.sqlite")  # Crea una connessione al database SQLite "database.sqlite"

    @abc.abstractmethod
    def getConnection(self):
        # Metodo astratto per ottenere l'oggetto di connessione al database
        pass

    def closeConnection(self):
        # Metodo per chiudere la connessione al database
        self.conn.close()  # Chiude la connessione al database SQLite