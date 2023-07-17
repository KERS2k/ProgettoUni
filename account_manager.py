import sqlite3
import hashlib
import secrets


class AccountManager:

    def __init__(self, db_manager):
        # Costruttore della classe AccountManager
        self.conn = db_manager.getConnection()  # Ottiene l'oggetto di connessione al database dal DbManager

    def register(self, name, surname, email, password):
        # Registra un nuovo utente nel database
        salt = secrets.token_hex(16)  # Genera un sale casuale
        hashed_password = self._hash_password(password, salt)  # Calcola l'hash della password utilizzando il sale generato

        query = '''INSERT INTO users_db (name, surname, email, salt, password)
                    VALUES (?, ?, ?, ?, ?)'''  # Query per l'inserimento dei dati dell'utente nel database
        try:
            self.conn.execute(query, (name, surname, email, salt, hashed_password))  # Esegue la query di inserimento
            self.conn.commit()  # Conferma le modifiche apportate al database
            return True  # Restituisce True se la registrazione è avvenuta con successo
        except sqlite3.IntegrityError:
            return False  # Restituisce False se si verifica un errore di integrità nel database

    def _hash_password(self, password, salt):
        # Calcola l'hash della password concatenata con il sale utilizzando l'algoritmo SHA256
        salted_password = (password + salt).encode()  # Concatena la password con il sale e codifica in bytes
        hashed_password = hashlib.sha256(salted_password).hexdigest()  # Calcola l'hash della password
        return hashed_password  # Restituisce l'hash risultante

    def login(self, email, password):
        # Effettua il login dell'utente
        query = '''SELECT * FROM users_db WHERE email = ?'''  # Query per ottenere i dati dell'utente corrispondente all'email
        cursor = self.conn.execute(query, (email,))  # Esegue la query
        user = cursor.fetchone()  # Ottiene il record dell'utente trovato

        if user is None:
            return False  # Restituisce False se l'utente non esiste nel database

        _, _, _, _, salt, hashed_password = user #_, _, _, _, sono placeholder
        if self._hash_password(password, salt) == hashed_password:
            return True  # Restituisce True se la password fornita corrisponde all'hash memorizzato nel database
        else:
            return False  # Restituisce False se la password non corrisponde

    def get_user_id(self, email):
        # Ottiene l'ID dell'utente dato l'email
        query = "SELECT id FROM users_db WHERE email = ?"  # Query per ottenere l'ID dell'utente
        cursor = self.conn.execute(query, (email,))  # Esegue la query
        result = cursor.fetchone()  # Ottiene il risultato della query

        if result:
            return result[0]  # Restituisce l'ID dell'utente se presente
        else:
            return None  # Restituisce None se l'utente non è presente nel database