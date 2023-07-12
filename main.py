from account_manager import AccountManager
from game_manager import GameManager
from library import Library
import sys

def main():


    account_manager = AccountManager()
    game_manager = GameManager()
    library = Library()

    while True:
        # Display main menu options
        print("1. Log in")
        print("2. Register")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":  # Log in
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if account_manager.login(email, password):
                user_id = account_manager.get_user_id(email)  # Retrieve user ID
                print("Login successful.")

                while True:
                    # Display secondary menu options
                    print("1. Print database")
                    print("2. Get game record")
                    print("3. Print records by user ID")
                    print("4. Exit")

                    sub_choice = input("Select an option: ")

                    if sub_choice == "1":  # Print database
                        game_manager.print_all_database()

                    elif sub_choice == "2":  # Get game record
                        while True:
                            game_id = input("Enter the game ID (or 'q' to quit): ")
                            if game_id == 'q':
                                break

                            try:
                                game_id = int(game_id)
                                record = game_manager.get_game_record(game_id)
                                if record:
                                    print("Game record:")
                                    print(record)

                                    # Ask for status if inserting a new record
                                    insert_choice = input("Do you want to insert a new record? (y/n): ")
                                    if insert_choice.lower() == "y":
                                        status = input("Enter the status: ")
                                        library.insert_record(user_id, game_id, status)
                                else:
                                    print("Game not found.")
                                break
                            except ValueError:
                                print("Invalid game ID. Please enter a valid integer.")

                    elif sub_choice == "3":  # Print records by user ID
                        records = library.get_records_by_user_id(user_id)
                        if records:
                            print("Records for User ID:", user_id)
                            for record in records:
                                print(record)
                        else:
                            print("No records found for User ID:", user_id)

                    elif sub_choice == "4":  # Exit
                        print("Exiting the program.")
                        account_manager.close_connection()
                        game_manager.close_connection()
                        library.close_connection()
                        sys.exit()

                    else:
                        print("Invalid choice. Please try again.")

                account_manager.close_connection()
                game_manager.close_connection()
                library.close_connection()

            else:
                print("Login failed. Please try again.")

        elif choice == "2":  # Register
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if account_manager.register(name, surname, email, password):
                print("Registration successful.")
            else:
                print("Registration failed. Please try again.")

        elif choice == "3":  # Exit
            print("Exiting the program.")
            account_manager.close_connection()
            game_manager.close_connection()
            library.close_connection()
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()