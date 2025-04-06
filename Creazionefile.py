# Creazionefile.py

def crea_file(nome_file):
    with open(nome_file, 'w') as file:
        file.write("Questo è un file di esempio.\n")
        file.write("Puoi aggiungere altre righe di testo qui.\n")

def leggi_file(nome_file):
    with open(nome_file, 'r') as file:
        contenuto = file.read()
    return contenuto

def main():
    nome_file = 'esempio.txt'
    
    # Creazione e scrittura del file
    crea_file(nome_file)
    print(f"File '{nome_file}' creato e scritto con successo.")
    
    # Lettura del file
    contenuto = leggi_file(nome_file)
    print(f"Contenuto del file '{nome_file}':\n{contenuto}")

if __name__ == "__main__":
    main()