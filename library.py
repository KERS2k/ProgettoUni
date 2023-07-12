import sqlite3

class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS library (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    game_id INTEGER NOT NULL,
                    status TEXT
                )'''
        self.conn.execute(query)
        self.conn.commit()

    def insert_record(self, user_id, game_id, status):
        query = '''INSERT INTO library (user_id, game_id, status)
                    VALUES (?, ?, ?)'''
        try:
            self.conn.execute(query, (user_id, game_id, status))
            self.conn.commit()
            print("Record inserted successfully.")
        except sqlite3.IntegrityError:
            print("Error: Record already exists or invalid values.")

    def get_records_by_user_id(self, user_id):
        query = '''SELECT * FROM library WHERE user_id = ?'''
        cursor = self.conn.execute(query, (user_id,))
        records = cursor.fetchall()
        return records

    def close_connection(self):
        self.conn.close()