class GameManager:
    def __init__(self, db_manager):
        # Costruttore della classe GameManager
        # Prende un oggetto db_manager come argomento
        self.conn = db_manager.getConnection()  # Ottiene la connessione al database dal db_manager

    def print_all_videogames(self):
        # Metodo per stampare tutti i videogiochi presenti nel database
        cursor = self.conn.cursor()  # Crea un cursore per eseguire le query
        cursor.execute('SELECT * FROM videogames_db')  # Esegue una query per selezionare tutti i record dalla tabella "videogames_db"
        rows = cursor.fetchall()  # Recupera tutti i risultati della query

        # Itera sui risultati e stampa le informazioni di ogni videogioco
        for row in rows:
            game_id, game, producer, genre, release_date = row
            print(f"ID: {game_id}")
            print(f"Game: {game}")
            print(f"Producer: {producer}")
            print(f"Genre: {genre}")
            print(f"Release Date: {release_date}")
            print()

    def get_game_record(self, game_id):
        # Metodo per ottenere il record di un videogioco dato il suo ID
        cursor = self.conn.cursor()  # Crea un cursore per eseguire le query
        query = "SELECT name FROM videogames_db WHERE id = ?"  # Query per selezionare il nome del videogioco corrispondente all'ID specificato
        cursor.execute(query, (game_id,))  # Esegue la query con l'ID come parametro
        record = cursor.fetchone()  # Recupera il primo risultato della query

        return record  # Restituisce il record del videogioco