class GameManager:

    def __init__(self, db_manager):
        self.conn = db_manager.getConnection()

    def print_all_videogames(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM videogames_db')
        rows = cursor.fetchall()
        for row in rows:
            game_id, game, producer, genre, release_date = row
            print(f"ID: {game_id}")
            print(f"Game: {game}")
            print(f"Producer: {producer}")
            print(f"Genre: {genre}")
            print(f"Release Date: {release_date}")
            print()


    def get_game_record(self, game_id):
        cursor = self.conn.cursor()
        query = "SELECT name FROM videogames_db WHERE id = ?"
        cursor.execute(query, (game_id, ))
        record = cursor.fetchone()
        return record  
    
