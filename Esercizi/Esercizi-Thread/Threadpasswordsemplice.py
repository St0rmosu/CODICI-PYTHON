import threading                                                                # Per usare i thread
from hashlib import sha256                                                      # Per calcolare l'hash delle password

# Funzione che controlla se l'hash della password è in un chunk
def controlla_chunk(chunk, hash_password, risultato, lock):
    for password in chunk:
        # Calcola l'hash della password del file
        hash_corrente = sha256(password.encode()).hexdigest()
        
        if hash_corrente == hash_password:
            with lock:                                                          # Blocchiamo l'accesso per evitare problemi tra thread
                risultato.append(True)
            return                                                              # Uscita anticipata: trovato!

# Funzione principale
def controlla_password(nomefile, password_da_cercare, chunk_size=4096):
    # Calcoliamo l'hash della password da cercare
    hash_password = sha256(password_da_cercare.encode()).hexdigest()

    # Apriamo il file e leggiamo le righe
    with open(nomefile, 'r', encoding='utf-8', errors='ignore') as file:
        tutte_le_password = file.read().splitlines()

    # Dividiamo la lista in chunk
    chunks = [tutte_le_password[i:i + chunk_size] for i in range(0, len(tutte_le_password), chunk_size)]

    risultato = []                                                             # Lista che ci dirà se abbiamo trovato la password
    threads = []                                                               # Qui salviamo tutti i thread
    lock = threading.Lock()                                                    # Per proteggere l'accesso a 'risultato'

    # Creiamo un thread per ogni chunk
    for chunk in chunks:
        t = threading.Thread(target=controlla_chunk, args=(chunk, hash_password, risultato, lock))
        threads.append(t)
        t.start()

    # Aspettiamo che tutti i thread finiscano
    for t in threads:
        t.join()

    return True in risultato                                                   # Se abbiamo almeno un True, la password è stata trovata

# Programma principale
if __name__ == '__main__':
    nomefile = 'rockyou.txt'                                                   # Cambia con il nome corretto del file se diverso
    password = input("Inserisci la password da controllare: ")

    if controlla_password(nomefile, password):
        print("La password è presente nel dizionario! Cambiala!")
    else:
        print("La password NON è nel dizionario.")