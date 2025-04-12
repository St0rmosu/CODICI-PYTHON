def acquisisci_dati():
    nomi = []
    eta = []
    while True:
        nome = input("Inserisci un nome (lascia vuoto per terminare): ")
        if nome == '':
            break
        età = int(input("Inserisci l'età: "))
        nomi.append(nome)
        eta.append(età)
    return nomi, eta

def calcola_statistiche(nomi, eta):
    numero_nomi = len(nomi)
    media_eta = sum(eta) / len(eta) if eta else 0
    return numero_nomi, media_eta

def salva_su_file(nomi, eta):
    numero_nomi, media_eta = calcola_statistiche(nomi, eta)
    with open('nomi.txt', 'w') as file_nomi:
        file_nomi.write(f"Numero di nomi: {numero_nomi}\n")
        file_nomi.write("\n".join(nomi))
    with open('eta.txt', 'w') as file_eta:
        file_eta.write(f"Età media: {media_eta:.2f}\n")
        file_eta.write("\n".join(map(str, eta)))

def main():
    nomi, eta = acquisisci_dati()
    salva_su_file(nomi, eta)

if __name__ == "__main__":
    main()
