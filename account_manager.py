import sqlite3
import hashlib
import secrets

class AccountManager:
    def __init__(self, db):
        self.conn = db.getConnection()

    def register(self, name, surname, email, password):
        salt = secrets.token_hex(16)
        hashed_password = self._hash_password(password, salt)

        query = '''INSERT INTO users (name, surname, email, salt, password)
                    VALUES (?, ?, ?, ?, ?)'''
        try:
            self.conn.execute(query, (name, surname, email, salt, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("User with the provided email already exists.")
            return False

    def login(self, email, password):
        query = '''SELECT * FROM users WHERE email = ?'''
        cursor = self.conn.execute(query, (email,))
        user = cursor.fetchone()
        if user is None:
            print("Invalid email or password.")
            return False

        _, _, _, _, salt, hashed_password = user
        if self._hash_password(password, salt) == hashed_password:
            print("Login successful.")
            return True
        else:
            print("Invalid email or password.")
            return False

    def _hash_password(self, password, salt):
        salted_password = (password + salt).encode()
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password
    
    def get_account_info(self, account_id):
        query = '''SELECT * FROM users WHERE id = ?'''
        cursor = self.conn.execute(query, (account_id,))
        user = cursor.fetchone()
        if user is None:
            print("No user found with the provided ID.")
            return None

        account_id, name, surname, email, _, _ = user
        account_info = f"ID: {account_id}\nName: {name}\nSurname: {surname}\nEmail: {email}"
        return account_info
    
    def get_user_id(self, email):
        query = "SELECT id FROM users WHERE email = ?"
        cursor = self.conn.execute(query, (email,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def close_connection(self):
        self.conn.close()