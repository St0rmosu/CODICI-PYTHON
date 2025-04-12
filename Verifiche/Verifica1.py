"""
Traccia 1 :
    Scrivere il file con un nome scelto dall'utente  (es. Periferiche.txt) che contenga tutti i dispositivi Hardware che hanno come tipo "periferiche" 
    e un altro file con un nome scelto dall'utente (es. GPU.txt) che contenga tutti i dispositivi Hardware che hanno "GPU" come tipo di periferica.



    //Bonus\\
        
        Scrivere una funzione che parta da uno dei file .txt e restituisca il contenuto in una tabella .html
        (es. se si sceglie il file Periferiche.txt, la funzione restituirà una tabella html con tutte le periferiche)

"""

# Analisi

"""
    Obiettivo: Creare un codice che scriva due file con dispositivi hardware filtrati per tipo

    Dati in input:
    
    Lista di dispositivi hardware (lista di dizionari)                   => Questa lista conterrà i dispositivi hardware con i loro attributi
    Nome scelto dall'utente per il file delle periferiche (stringa)      => Questa stringa conterrà il nome del file per i dispositivi di tipo "periferiche"
    Nome scelto dall'utente per il file delle GPU (stringa)              => Questa stringa conterrà il nome del file per i dispositivi di tipo "GPU"

    Dati in output:

    File delle periferiche (file di testo)                               => Questo file conterrà tutti i dispositivi hardware di tipo "periferiche"
    File delle GPU (file di testo)                                       => Questo file conterrà tutti i dispositivi hardware di tipo "GPU"

    Ipotesi:
    
    La lista dei dispositivi hardware sarà fornita come input
    L'utente fornirà i nomi dei file per salvare i dispositivi filtrati
    Ogni dispositivo hardware avrà almeno un attributo "tipo" che può essere "periferiche" o "GPU"

    Funzioni:

    1. Prendere in input la lista dei dispositivi hardware
    2. Prendere in input il nome del file per le periferiche
    3. Prendere in input il nome del file per le GPU
    4. Filtrare i dispositivi hardware per tipo "periferiche"
    5. Filtrare i dispositivi hardware per tipo "GPU"
    6. Scrivere i dispositivi filtrati nel rispettivo file
    7. Stampare un messaggio di conferma per l'utente
    
    //BONUS\\
        
        8. Scrivere una funzione che parta da uno dei file .txt e restituisca il contenuto in una tabella .html

"""

#Pseudocodifica

"""
    1. Definire la lista dei dispositivi hardware
    2. Definire il nome del file per le periferiche
    3. Definire il nome del file per le GPU
    4. Filtrare i dispositivi hardware per tipo "periferiche""
    5. Filtrare i dispositivi hardware per tipo "GPU"
    6. Scrivere i dispositivi filtrati nel rispettivo file
    7. Stampare un messaggio di conferma per l'utente
    
    // BONUS \\
        
        8. Chiedere all'utente se vuole visualizzare il contenuto dei file in una tabella html
        9. Se l'utente risponde si, chiedere quale file vuole visualizzare
        10. Scrivere una funzione che parta da uno dei file .txt e restituisca il contenuto in una tabella .html
        11. Stampare la tabella html
    
"""

#Codice
# Prendere le periferiche dal file componenti_pc.txt
def prendi_periferiche(file):
    with open(file, "r") as f:
        periferiche = []
        for riga in f:
            if "periferiche" in riga.lower():
                periferiche.append(riga)
        return periferiche

# Prendere le GPU dal file componenti_pc.txt
def prendi_gpu(file):
    with open(file, "r") as f:
        gpu = []
        for riga in f:
            if "gpu" in riga.lower():
                gpu.append(riga)
        return gpu

# Scrivere le periferiche nel file Periferiche.txt
def scrivi_periferiche(file, periferiche):
    with open(file, "w") as f:
        for periferica in periferiche:
            f.write(periferica)
            
# Scrivere le GPU nel file GPU.txt
def scrivi_gpu(file, gpu):
    with open(file, "w") as f:
        for g in gpu:
            f.write(g)

# // BONUS \\
# Creare una tabella html con il contenuto dei file che si sceglie di visualizzare

def tabella_html(file, output_html):
    with open(file, "r") as f:
        tabella = "<table border='1'>\n"
        tabella += "  <tr><th>Nome</th><th>Tipo</th><th>Anno di produzione</th><th>Tipologia</th></th>Prezzo</tr>\n"
        for riga in f:
            tabella += "  <tr>\n"
            colonne = riga.split(",")
            for colonna in colonne:
                tabella += f"    <td>{colonna.strip()}</td>\n"
            tabella += "  </tr>\n"
        tabella += "</table>"
    
    with open(output_html, "w") as f:
        f.write(tabella)
    print(f"Tabella HTML creata con successo nel file {output_html}")

# Main
if __name__ == "__main__":
    periferiche = prendi_periferiche("componenti_pc.txt")
    gpu = prendi_gpu("componenti_pc.txt")
    scrivi_periferiche("Periferiche.txt", periferiche)
    scrivi_gpu("GPU.txt", gpu)
    print("File creati con successo!")
    
    # // BONUS \\
    risposta = input("Vuoi visualizzare il contenuto dei file in una tabella html? (si/no): ")
    if risposta.lower() == "si":
        file = input("Quale file vuoi visualizzare? (Periferiche.txt/GPU.txt): ")
        output_html = input("Inserisci il nome del file HTML di output (es. tabella.html): ")
        tabella_html(file, output_html)
    else:
        print("Arrivederci!")
