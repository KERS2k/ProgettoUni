import sqlite3
from game_manager import GameManager


class Library:

    def __init__(self, db_manager):
        # Costruttore della classe Library
        self.conn = db_manager.getConnection()  # Ottiene l'oggetto di connessione al database dal DbManager
        self.game_manager = GameManager(db_manager)  # Crea un'istanza di GameManager utilizzando db_manager come argomento

    def _insert_record(self, user_id, game_id, status):
        # Inserisce un nuovo record nella tabella "personal_library_db" con l'ID dell'utente, l'ID del gioco e lo stato specificato
        query = '''INSERT INTO personal_library_db (user_id, game_id, status) VALUES (?, ?, ?)'''
        try:
            self.conn.execute(query, (user_id, game_id, status))  # Esegue la query di inserimento
            self.conn.commit()  # Conferma le modifiche apportate al database
            print("Videogioco aggiunto correttamente alla propria libreria")
        except sqlite3.IntegrityError:
            print("Errore, gioco già presente nella libreria personale o i valori inseriti sono sbagliati")

    def add_game_to_personal_library(self, user_id):
        # Consente all'utente di aggiungere un gioco alla propria libreria personale
        while True:
            game_id = input("Inserisci l'ID del gioco da inserire nella propria libreria (oppure inserisci 'x' per uscire): ")
            if game_id == 'x':
                break

            try:
                game_id = int(game_id)
                record = self.game_manager.get_game_record(game_id)  # Ottiene il record del gioco utilizzando il GameManager
                if record:
                    print("Game record:")
                    print(record)

                    # Richiesta di inserire la nota se si vuole inserire il nuovo record
                    insert_choice = input("Confermi di voler inserire il gioco nella propria libreria? (s/n) ")
                    if insert_choice.lower() == "s":
                        status = input("Inserisci la nota: ")
                        self._insert_record(user_id, game_id, status)  # Chiama il metodo _insert_record per aggiungere il gioco alla libreria personale
                else:
                    print("Gioco non trovato")
                break
            except ValueError:
                print("Gioco non trovato")

    def _delete_record(self, user_id, game_id):
        # Elimina un record dalla tabella "personal_library_db" corrispondente all'ID dell'utente e all'ID del gioco specificati
        query = "DELETE FROM personal_library_db WHERE user_id = ? AND game_id = ?"
        try:
            self.conn.execute(query, (user_id, game_id))  # Esegue la query di eliminazione
            self.conn.commit()  # Conferma le modifiche apportate al database
            print("Videogioco cancellato correttamente dalla propria libreria")
        except sqlite3.Error:
            print("Errore, tentativo di cancellare il videogioco fallito")

    def delete_record_from_personal_library(self, user_id):
        # Consente all'utente di rimuovere un gioco dalla propria libreria personale
        while True:
            game_id = input("Inserisci l'ID del gioco da rimuovere dalla propria libreria (oppure inserisci 'x' per uscire): ")
            if game_id == 'x':
                break

            try:
                game_id = int(game_id)
                record = self._get_game_inside_library_record(user_id, game_id)  # Ottiene il record del gioco all'interno della libreria personale
                if record:
                    print("Videogioco: ")
                    print(record)

                    # Richiesta di conferma per la rimozione del gioco dalla libreria
                    delete_choice = input("Confermi di voler rimuovere il gioco dalla propria libreria? (s/n) ")
                    if delete_choice.lower() == "s":
                        self._delete_record(user_id, game_id)  # Chiama il metodo _delete_record per rimuovere il gioco dalla libreria personale
                else:
                    print("Gioco non trovato")
                break
            except ValueError:
                print("Gioco non trovato")

    def _get_game_inside_library_record(self, user_id, game_id):
        # Ottiene il record del gioco all'interno della libreria personale
        cursor = self.conn.cursor()
        query = '''SELECT lib.user_id, vid.name AS game_name, lib.status
                FROM personal_library_db AS lib
                JOIN videogames_db AS vid ON lib.game_id = vid.id
                WHERE lib.user_id = ? AND lib.game_id = ?'''
        cursor.execute(query, (user_id, game_id))  # Esegue la query
        record = cursor.fetchone()  # Ottiene il record

        return record

    def print_my_games(self, user_id):
        # Stampa i giochi presenti nella libreria personale dell'utente specificato
        query = '''SELECT lib.user_id, vid.name AS game_name, lib.status
                FROM personal_library_db AS lib
                JOIN videogames_db AS vid ON lib.game_id = vid.id
                WHERE lib.user_id = ?'''
        cursor = self.conn.execute(query, (user_id,))  # Esegue la query
        games = cursor.fetchall()  # Ottiene tutti i giochi

        if games:
            print("I miei giochi:")
            for game in games:
                print(game)  # Stampa i giochi
        else:
            print("Nessun videogioco salvato", user_id)

    def update_status(self, user_id, game_id):
        # Consente all'utente di aggiornare lo stato di un gioco nella propria libreria personale
        query = '''SELECT lib.user_id, vid.name AS game_name, lib.status
                    FROM personal_library_db AS lib
                    JOIN videogames_db AS vid ON lib.game_id = vid.id
                    WHERE lib.user_id = ? AND lib.game_id = ?'''
        cursor = self.conn.execute(query, (user_id, game_id))  # Esegue la query
        record = cursor.fetchone()  # Ottiene il record

        if record:
            print("Videogioco: ")
            print(record)
            new_status = input("Inserisci la nuova nota: ")

            update_query = "UPDATE personal_library_db SET status = ? WHERE user_id = ? AND game_id = ?"
            try:
                self.conn.execute(update_query, (new_status, user_id, game_id))  # Esegue la query di aggiornamento
                self.conn.commit()  # Conferma le modifiche apportate al database
                print("Nota aggiornata")
            except sqlite3.Error:
                print("Errore nell'aggiornare la nota")
        else:
            print("Nessun gioco salvato con l'ID fornito")