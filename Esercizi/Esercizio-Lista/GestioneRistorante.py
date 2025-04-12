import json

# File paths
menu_file = 'menu.json'
tables_file = 'tables.json'
orders_file = 'orders.json'

# Menu management
def add_menu_item():
    menu_item = {
        "id": input("Numero progressivo: "),
        "type": input("Tipo (primo, secondo, pizza, bevanda, etc..): "),
        "name": input("Nome del piatto: "),
        "ingredients": input("Ingredienti: "),
        "price": float(input("Costo di vendita: "))
    }
    with open(menu_file, 'a') as file:
        file.write(json.dumps(menu_item) + '\n')
    print("Piatto aggiunto al menù.")

# Table management
def add_table():
    table = {
        "table_number": input("Numero tavolo: "),
        "seats": int(input("Numero di coperti: "))
    }
    with open(tables_file, 'a') as file:
        file.write(json.dumps(table) + '\n')
    print("Tavolo aggiunto.")

# Order management
def add_order():
    order = {
        "table_number": input("Numero tavolo: "),
        "items": input("Inserisci gli ID dei piatti ordinati separati da una virgola: ").split(',')
    }
    with open(orders_file, 'a') as file:
        file.write(json.dumps(order) + '\n')
    print("Ordine aggiunto.")

# Main menu
def main():
    while True:
        print("\nGestione Ristorante")
        print("1. Aggiungi piatto al menù")
        print("2. Aggiungi tavolo")
        print("3. Aggiungi ordine")
        print("4. Esci")
        choice = input("Scegli un'opzione: ")

        if choice == '1':
            add_menu_item()
        elif choice == '2':
            add_table()
        elif choice == '3':
            add_order()
        elif choice == '4':
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()