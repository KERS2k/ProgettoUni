import sqlite3

class GameManager:
    def __init__(self, db):
        self.conn = db.getConnection()

    def print_all_database(self):
        cursor = self.conn.cursor()

        cursor.execute('SELECT * FROM videogames')
        rows = cursor.fetchall()

        for row in rows:
            game_id, game, producer, genre, release_date = row
            print(f"ID: {game_id}")
            print(f"Game: {game}")
            print(f"Producer: {producer}")
            print(f"Genre: {genre}")
            print(f"Release Date: {release_date}")
            print()


    def get_game_record(self, game_name):
        cursor = self.conn.cursor()
        query = "SELECT name FROM VideoGames WHERE id = ?"
        cursor.execute(query, (game_name,))
        record = cursor.fetchone()
        return record  # Return the game name
    
    def get_game_name(self, game_id):
        cursor = self.conn.cursor()
        query = "SELECT name FROM VideoGames WHERE id = ?"
        cursor.execute(query, (game_id,))
        record = cursor.fetchone()

        if record:
            game_name = record[0]
            return game_name
        else:
            return None
