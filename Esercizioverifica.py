import random

DIMENSIONE_ARRAY = 20
NUMERO_TENTATIVI = 5

def inizializza_mappa():
    mappa = [0] * DIMENSIONE_ARRAY

    # Posiziona il tesoro
    posizione_tesoro = random.randint(0, DIMENSIONE_ARRAY - 1)
    mappa[posizione_tesoro] = 9

    # Posiziona le trappole
    for _ in range(5):
        posizione_trappola = random.randint(0, DIMENSIONE_ARRAY - 1)
        while mappa[posizione_trappola] != 0:
            posizione_trappola = random.randint(0, DIMENSIONE_ARRAY - 1)
        mappa[posizione_trappola] = 1

    return mappa

def stampa_mappa(mappa, mostra):
    for i in range(DIMENSIONE_ARRAY):
        if mostra:
            print(f"[{mappa[i]}]", end=" ")
        else:
            print("[?]", end=" ")
    print()

def gioca_turno(mappa, tentativi):
    scelta = int(input(f"Scegli una posizione (0-{DIMENSIONE_ARRAY - 1}): "))

    if scelta < 0 or scelta >= DIMENSIONE_ARRAY:
        print("Scelta non valida! Prova di nuovo.")
        return tentativi, False

    if mappa[scelta] == 9:
        print("Hai trovato il tesoro!")
        return tentativi, True
    elif mappa[scelta] == 1:
        print("Oh no! Hai trovato una trappola. Perdi un tentativo.")
        tentativi -= 1
    else:
        print("Posizione vuota. Sei al sicuro.")

    print(f"Tentativi rimanenti: {tentativi}")
    return tentativi, False

def main():
    mappa = inizializza_mappa()
    tentativi = NUMERO_TENTATIVI
    trovato = False

    print("Benvenuto a Caccia al Tesoro!")
    print("Devi trovare il tesoro (9) evitando le trappole (1).")
    print(f"Hai {NUMERO_TENTATIVI} tentativi. Buona fortuna!")

    while tentativi > 0 and not trovato:
        tentativi, trovato = gioca_turno(mappa, tentativi)

    if trovato:
        print("Complimenti, hai trovato il tesoro! Hai vinto!")
    else:
        print("Hai esaurito i tentativi. Hai perso!")

if __name__ == "__main__":
    main()