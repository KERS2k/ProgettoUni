import sqlite3

class Library:
    def __init__(self, db):
        self.conn = db.getConnection()

    def insert_record(self, user_id, game_name, status):
        query = '''INSERT INTO library (user_id, game_name, status)
                    VALUES (?, ?, ?)'''
        try:
            self.conn.execute(query, (user_id, game_name, status))
            self.conn.commit()
            print("Record inserted successfully.")
        except sqlite3.IntegrityError:
            print("Error: Record already exists or invalid values.")

    def get_records_by_user_id(self, user_id):
        query = '''SELECT * FROM library WHERE user_id = ?'''
        cursor = self.conn.execute(query, (user_id,))
        records = cursor.fetchall()
        return records
