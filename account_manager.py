import sqlite3
import hashlib
import secrets

class AccountManager:

    def __init__(self, db_manager):
        self.conn = db_manager.getConnection()





    def register(self, name, surname, email, password):
        salt = secrets.token_hex(16)
        hashed_password = self._hash_password(password, salt)

        query = '''INSERT INTO users_db (name, surname, email, salt, password)
                    VALUES (?, ?, ?, ?, ?)'''
        try:
            self.conn.execute(query, (name, surname, email, salt, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def _hash_password(self, password, salt):
        salted_password = (password + salt).encode()
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password
    



    def login(self, email, password):
        query = '''SELECT * FROM users_db WHERE email = ?'''
        cursor = self.conn.execute(query, (email,))
        user = cursor.fetchone()
        if user is None:
            return False

        _, _, _, _, salt, hashed_password = user
        if self._hash_password(password, salt) == hashed_password:
            return True
        else:
            return False
    
    def get_user_id(self, email): 
        query = "SELECT id FROM users_db WHERE email = ?"
        cursor = self.conn.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
