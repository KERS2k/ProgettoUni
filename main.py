from run_application import RunApplication
from concrete_db_manager import ConcreteDbManager


def main():
    # Creazione di un'istanza di ConcreteDbManager
    db_manager = ConcreteDbManager()

    # Creazione di un'istanza di RunApplication
    app = RunApplication(db_manager)

    # Esecuzione del ciclo principale dell'applicazione
    app.run()

# Funzione principale che avvia l'applicazione
main()