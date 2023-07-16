from db_manager import DbManager
from account_manager import AccountManager
from game_manager import GameManager
from personal_library_manager import Library
import sys

class RunApplication:

    def __init__(self):
        db_manager = DbManager()
        account_manager = AccountManager(db_manager)
        game_manager = GameManager(db_manager)
        library = Library(db_manager)

        self.db_manager = db_manager
        self.account_manager = account_manager
        self.game_manager = game_manager
        self.personal_library_manager = library


    
    def run(self):
        while True:
            self.primary_menu()



    def primary_menu(self):
        #Menu 1
        print("1. Log in")
        print("2. Registrati")
        print("3. Esci")

        choice = input("Selezione un'opzione: ")

        if choice == "1":  # Log in
            email = input("Email: ")
            password = input("Password: ")
            if self.account_manager.login(email, password):
                print("Log in effettuato con successo")
                user_id = self.account_manager.get_user_id(email)
                self.secondary_menu(user_id)
            else:
                print("Errore durante il login. Riprova.")

        elif choice == "2":  # Registrazione
            name = input("Nome: ")
            surname = input("Cognome: ")
            email = input("Email: ")
            password = input("Password: ")
            if self.account_manager.register(name, surname, email, password):
                print("Registrazione effettuata con successo")
                user_id = self.account_manager.get_user_id(email) 
                self.secondary_menu(user_id)
            else:
                print("Errore durante la registrazione. Riprova.")

        elif choice == "3":  # Exit
            self.exit_program()

        else:
            print("Scelta invalida, si chiede di riprovare")

    def secondary_menu(self, user_id):
        while True:
            # Menu 2
            print("1. Stampa l'elenco di videogiochi disponibili")
            print("2. Aggiungi un gioco alla tua libreria personale")
            print("3. Rimuovi un gioco dalla tua libreria personale")
            print("4. Stampa l'elenco dei miei videogiochi")
            print("5. Aggiorna nota")
            print("6. Logout")

            sub_choice = input("Selezione un'opzione: ")

            if sub_choice == "1":
                self.game_manager.print_all_videogames()

            elif sub_choice == "2":
                self.personal_library_manager.add_game_to_personal_library(user_id)

            elif sub_choice == "3":
                self.personal_library_manager.delete_record_from_personal_library(user_id)

            elif sub_choice == "4":
                self.personal_library_manager.print_my_games(user_id)

            elif sub_choice == "5":
                game_id = input("Inserisci l'ID del gioco da modificare: ")
                self.personal_library_manager.update_status(user_id, int(game_id))

            elif sub_choice == "6":
                print("Log out")
                break
            else:
                print("Scelta invalida, si chiede di riprovare")

    def exit_program(self):
        print("Chiusura del programma...")
        self.db_manager.closeConnection()
        sys.exit()