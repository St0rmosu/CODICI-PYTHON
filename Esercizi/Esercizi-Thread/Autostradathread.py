import threading
import random
import time

def thread_telepass(semaforo: threading.Semaphore, auto: int, targa: str):
    print(f"L'auto {auto} con ({targa}) sta occupando il casello telepass")
    semaforo.acquire()  # Acquisisce il semaforo
    time.sleep(random.randint(1, 3))  # Simula il tempo di passaggio
    semaforo.release()  # Rilascia il semaforo
    print(f"L'auto {auto} ({targa}) ha liberato il casello telepass")

def thread_contanti(semaforo: threading.Semaphore, auto: int, targa: str):
    print(f"L'auto {auto} con ({targa}) sta occupando il casello contanti")
    semaforo.acquire()  # Acquisisce il semaforo
    time.sleep(random.randint(3, 6))  # Simula il tempo di passaggio
    semaforo.release()  # Rilascia il semaforo
    print(f"L'auto {auto} ({targa}) ha liberato il casello contanti")

def thread_carta(semaforo: threading.Semaphore, auto: int, targa: str):
    print(f"L'auto {auto} ({targa}) sta occupando il casello carta di credito")
    semaforo.acquire()  # Acquisisce il semaforo
    time.sleep(random.randint(2, 4))  # Simula il tempo di passaggio
    semaforo.release()  # Rilascia il semaforo
    print(f"L'auto {auto} ({targa}) ha liberato il casello carta di credito")

def CreazioneTarga():
    targa = ""
    for i in range(3):
        targa += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(3):
        targa += random.choice("0123456789")
    for i in range(2):
        targa += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return targa

def main():
    Auto = 200
    PercentualeTelepass = 0.2
    PercentualeContanti = 0.4
    PercentualeCarta = 0.4
    ls_THREAD = []  # Lista per memorizzare i thread

    # Numero dei caselli
    NumeroCaselliTelepass = 1  # Numero di caselli per il telepass
    NumeroCaselliContanti = 2  # Numero di caselli per i contanti
    NumeroCaselliCarta = 1  # Numero di caselli per la carta di credito

    NumeroAutoPassantiTelepass = int(Auto * PercentualeTelepass)  # Calcola il numero di auto che passano con il telepass
    NumeroAutoPassantiContanti = int(Auto * PercentualeContanti)  # Calcola il numero di auto che passano con i contanti
    NumeroAutoPassantiCarta = int(Auto * PercentualeCarta)  # Calcola il numero di auto che passano con la carta di credito

    # Creazione dei semafori
    SemaforoTelepass = threading.Semaphore(NumeroCaselliTelepass)  # Semaforo per il telepass
    SemaforoContanti = threading.Semaphore(NumeroCaselliContanti)  # Semaforo per i contanti
    SemaforoCarta = threading.Semaphore(NumeroCaselliCarta)  # Semaforo per la carta di credito

    for i in range(NumeroAutoPassantiTelepass):
        targa = CreazioneTarga()
        t = threading.Thread(target=thread_telepass, args=(SemaforoTelepass, i + 1, targa))
        ls_THREAD.append(t)

    for i in range(NumeroAutoPassantiContanti):
        targa = CreazioneTarga()
        t = threading.Thread(target=thread_contanti, args=(SemaforoContanti, i + 1, targa))
        ls_THREAD.append(t)

    for i in range(NumeroAutoPassantiCarta):
        targa = CreazioneTarga()
        t = threading.Thread(target=thread_carta, args=(SemaforoCarta, i + 1, targa))
        ls_THREAD.append(t)

    for elemento in ls_THREAD:
        elemento.start()

    for elemento in ls_THREAD:
        elemento.join()

    print("Tutte le auto hanno passato il casello")
    print("Fine del programma")

if __name__ == "__main__":
    main()