import threading
from hashlib import sha256

# 🔧 Funzione per calcolare l'hash SHA256 di una stringa
def calculate_hash(string: str) -> str:
    return sha256(string.encode("latin-1")).hexdigest()

# 💥 Funzione che ogni thread esegue: cerca l'hash in un chunk
def cerca_password(chunk, hash_da_trovare, trovato_flag, lock):
    for password in chunk:
        if trovato_flag[0]:  # Se un altro thread ha già trovato la password, esco
            return
        
        if calculate_hash(password.strip()) == hash_da_trovare:
            with lock:
                if not trovato_flag[0]:  # Controllo di nuovo dentro il lock
                    print(f"✅ Password trovata: {password}")
                    trovato_flag[0] = True
            return

# 🧠 Funzione principale
def trova_password(nomefile, hash_da_trovare, chunk_size=4096):
    # Leggiamo il file
    with open(nomefile, 'r', encoding='utf-8', errors='ignore') as file:
        righe = file.readlines()

    # Dividiamo in chunk
    chunks = [righe[i:i + chunk_size] for i in range(0, len(righe), chunk_size)]

    lock = threading.Lock()
    trovato_flag = [False]         # Usiamo una lista per condividere il valore tra thread
    threads = []
    max_thread = 10                # Max 10 thread alla volta
    i = 0

    # Avviamo i thread a gruppi di 10
    while i < len(chunks) and not trovato_flag[0]:
        threads = []
        for j in range(max_thread):
            if i >= len(chunks) or trovato_flag[0]:
                break
            t = threading.Thread(target=cerca_password, args=(chunks[i], hash_da_trovare, trovato_flag, lock))
            threads.append(t)
            t.start()
            i += 1

        for t in threads:
            t.join()  # Aspettiamo che i thread del gruppo finiscano

    if not trovato_flag[0]:
        print("❌ La password NON è stata trovata.")

# 🚀 Avvio del programma
if __name__ == '__main__':
    hash_target = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
    file_path = "rockyou.txt"  # Assicurati che il file sia nella stessa cartella

    trova_password(file_path, hash_target)
