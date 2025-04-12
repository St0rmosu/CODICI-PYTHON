def addizione(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: divisione per zero"

def calcolatrice():
    print("Benvenuto nella calcolatrice Python!")
    print("Operazioni disponibili:")
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")

    while True:
        try:
            scelta = int(input("Scegli l'operazione (1/2/3/4) o 0 per uscire: "))
            if scelta == 0:
                print("Grazie per aver usato la calcolatrice. Arrivederci!")
                break

            if scelta not in [1, 2, 3, 4]:
                print("Scelta non valida. Riprova.")
                continue

            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))

            if scelta == 1:
                print(f"Risultato: {addizione(num1, num2)}")
            elif scelta == 2:
                print(f"Risultato: {sottrazione(num1, num2)}")
            elif scelta == 3:
                print(f"Risultato: {moltiplicazione(num1, num2)}")
            elif scelta == 4:
                print(f"Risultato: {divisione(num1, num2)}")

        except ValueError:
            print("Errore: inserisci un numero valido.")