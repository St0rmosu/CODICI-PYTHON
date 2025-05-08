# Traccia
"""
Un supermercato ha 3 tipi di casse:
1. Cassa tradizionale
2. Cassa per pagamento veloce
3. Cassa per donne incinta

Utilizzando la libreria threading e i semafori, scrivere un programma Python che simuli una coda di 100 utenti, 
50 dei quali useranno una cassa tradizionale, 30 la cassa per il pagamento veloce e 20 la cassa per donne incinte.

Devono essere soddisfati i seguenti requisiti:
1. Ogni utente deve essere identificato da un nome univoco
2. Il programma deve segnalare quando il cliente occupa la cassa
3. Ogni utente occupa la cassa per un tempo che varia da 1 a 10 secondi
4. Ogni utente ha una spesa media di 30 euro 
5. Il programma deve comunicare quando il cliente lascia la cassa 
6. Il programma deve stampare a fine giornata quanto ha incassato una determinata tipologia di cassa.
"""

# Analisi

"""
Obiettivo: Creare un programma che simuli il comportamento di un supermercato con 3 tipi di casse e calcoli l'incasso totale per ogni tipologia di cassa.

Dati in input:

- Numero totale di clienti (intero)                                         => 100 clienti
- Percentuale di clienti per ogni tipo di cassa (float)                     => 50% tradizionale, 30% pagamento veloce, 20% donne incinta
- Tempo di occupazione della cassa per ogni cliente (float)                 => Variabile tra 1 e 10 secondi
- Spesa media per cliente (float)                                           => 30 euro

Dati in output:

- Messaggi che indicano quando un cliente occupa e lascia la cassa
- Incasso totale per ogni tipologia di cassa

Ipotesi:

- Ogni cliente è identificato da un ID univoco
- Le percentuali di distribuzione dei clienti sono rispettate
- Ogni cassa ha un numero limitato di postazioni (semafori)

Funzioni:

1. Simulare il passaggio di un cliente alla cassa tradizionale
2. Simulare il passaggio di un cliente alla cassa per pagamento veloce
3. Simulare il passaggio di un cliente alla cassa per donne incinta
4. Calcolare l'incasso totale per ogni tipologia di cassa
5. Stampare i risultati finali
"""

# Pseudocodifica

"""
1. Definire il numero totale di clienti
2. Definire le percentuali di distribuzione dei clienti per ogni tipo di cassa
3. Calcolare il numero di clienti per ogni tipo di cassa
4. Creare semafori per ogni tipo di cassa
5. Generare thread per simulare il passaggio dei clienti alle casse
6. Ogni thread simula il comportamento di un cliente:
    - Occupa la cassa
    - Attende un tempo casuale tra 1 e 10 secondi
    - Aggiorna l'incasso totale della cassa
    - Rilascia la cassa
7. Stampare i messaggi di occupazione e rilascio della cassa
8. Calcolare e stampare l'incasso totale per ogni tipologia di cassa
"""


# Importo le librerie necessarie per il programma
import threading                                                                                                                # Per gestire i thread
import time                                                                                                                     # Per gestire i tempi di attesa
import random                                                                                                                   # Per generare numeri casuali# Importo le librerie necessarie per il programma

# Variabili globali per tenere traccia dei soldi incassati da ogni tipo di cassa
incasso_tradizionale = 0
incasso_veloce = 0
incasso_incinta = 0

def CreazioneNomeeCognome():
    """Questa funzione crea nomi e cognomi casuali per i clienti"""
    # Liste per il nome e cognome dei clienti
    nomi = ["Mario", "Luigi", "Giovanni", "Antonio", "Francesco", "Giuseppe", "Paolo", 
            "Marco", "Andrea", "Luca", "Sofia", "Maria", "Anna", "Giulia", "Laura", 
            "Giorgia", "Elena", "Sara", "Chiara", "Martina"]
    cognomi = ["Rossi", "Bianchi", "Verdi", "Neri", "Gialli", "Ferrari", "Esposito", 
               "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno", "Gallo", 
               "Conti", "De Luca", "Costa", "Giordano", "Mancini", "Rizzo"]
    # Ritorno un nome e cognome casuale dalle liste
    return f"{random.choice(nomi)} {random.choice(cognomi)}"

def thread_cassa_tradizionale(semaforo, nome_cliente, spesa):
    """Questa funzione gestisce i clienti alla cassa normale"""
    global incasso_tradizionale                                                                                                 # Uso la variabile globale per l'incasso
    with semaforo:                                                                                                              # Uso il semaforo per gestire l'accesso alla cassa
        print(f"{nome_cliente} sta occupando la cassa tradizionale.")
        tempo_attesa = random.uniform(1, 10)                                                                                    # Genero un tempo casuale tra 1 e 10 secondi
        time.sleep(tempo_attesa)                                                                                                # Faccio aspettare il cliente
        incasso_tradizionale += spesa                                                                                           # Aggiungo la spesa all'incasso totale
        print(f"{nome_cliente} ha lasciato la cassa tradizionale dopo {tempo_attesa:.1f} secondi. Spesa: {spesa:.2f}€")

def thread_cassa_pagamento_veloce(semaforo, nome_cliente, spesa):
    """Questa funzione gestisce i clienti alla cassa veloce"""
    global incasso_veloce
    with semaforo:
        print(f"{nome_cliente} sta occupando la cassa veloce.")
        tempo_attesa = random.uniform(1, 10)
        time.sleep(tempo_attesa)
        incasso_veloce += spesa
        print(f"{nome_cliente} ha lasciato la cassa veloce dopo {tempo_attesa:.1f} secondi. Spesa: {spesa:.2f}€")

def thread_cassa_donne_incinta(semaforo, nome_cliente, spesa):
    """Questa funzione gestisce i clienti alla cassa per donne incinta"""
    global incasso_incinta
    with semaforo:
        print(f"{nome_cliente} sta occupando la cassa per donne incinta.")
        tempo_attesa = random.uniform(1, 10)
        time.sleep(tempo_attesa)
        incasso_incinta += spesa
        print(f"{nome_cliente} ha lasciato la cassa per donne incinta dopo {tempo_attesa:.1f} secondi. Spesa: {spesa:.2f}€")

def Main():
    # Definisco il numero totale di clienti e come sono distribuiti
    Clienti = 100
    NumeroClientiTradizionali = 50                                                                                              # 50% dei clienti
    NumeroClientiPagamentoVeloce = 30                                                                                           # 30% dei clienti
    NumeroClientiDonneIncinta = 20                                                                                              # 20% dei clienti

    # Definisco quante casse ci sono per ogni tipo
    NumeroCasseTradizionali = 3
    NumeroCassePagamentoVeloce = 2
    NumeroCasseDonneIncinta = 1

    # Creo i semafori per gestire l'accesso alle casse
    SemaforoTradizionale = threading.Semaphore(NumeroCasseTradizionali)
    SemaforoPagamentoVeloce = threading.Semaphore(NumeroCassePagamentoVeloce)
    SemaforoDonneIncinta = threading.Semaphore(NumeroCasseDonneIncinta)

    ls_THREAD = []                                                                                                              # Lista per tenere tutti i thread
    start_time = time.time()                                                                                                    # Segno quando inizia la simulazione

    # Creo i thread per i clienti che useranno le casse tradizionali
    for i in range(NumeroClientiTradizionali):
        spesa = random.uniform(25, 35)                                                                                          # Genero una spesa casuale tra 25 e 35 euro
        nome = CreazioneNomeeCognome()                                                                                          # Creo un nome casuale per il cliente
        t = threading.Thread(target=thread_cassa_tradizionale, 
                           args=(SemaforoTradizionale, nome, spesa))
        ls_THREAD.append(t)

    # Faccio lo stesso per le casse veloci
    for i in range(NumeroClientiPagamentoVeloce):
        spesa = random.uniform(25, 35)
        nome = CreazioneNomeeCognome()
        t = threading.Thread(target=thread_cassa_pagamento_veloce, 
                           args=(SemaforoPagamentoVeloce, nome, spesa))
        ls_THREAD.append(t)

    # E per le casse delle donne incinta
    for i in range(NumeroClientiDonneIncinta):
        spesa = random.uniform(25, 35)
        nome = CreazioneNomeeCognome()
        t = threading.Thread(target=thread_cassa_donne_incinta, 
                           args=(SemaforoDonneIncinta, nome, spesa))
        ls_THREAD.append(t)

    # Avvio tutti i thread
    for t in ls_THREAD:
        t.start()
    # Aspetto che tutti i thread finiscano
    for t in ls_THREAD:
        t.join()

    # Stampo i risultati finali con tutti gli incassi
    print("\nRISULTATI FINALI:")
    print(f"Incasso totale casse tradizionali: {incasso_tradizionale:.2f}€")
    print(f"Incasso totale casse veloci: {incasso_veloce:.2f}€")
    print(f"Incasso totale casse donne incinta: {incasso_incinta:.2f}€")
    print(f"Incasso totale supermercato: {incasso_tradizionale + incasso_veloce + incasso_incinta:.2f}€")
    print(f"Tempo totale di simulazione: {time.time() - start_time:.2f} secondi")

# Eseguo il programma solo se viene eseguito direttamente
if __name__ == "__main__":
    Main()
