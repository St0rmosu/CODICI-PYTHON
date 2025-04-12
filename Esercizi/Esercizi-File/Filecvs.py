import csv

# Acquisizione dei dati dall'utente
nome = input("Inserisci il nome: ")
cognome = input("Inserisci il cognome: ")
eta = input("Inserisci l'età: ")
altezza = input("Inserisci l'altezza: ")

# Scrittura dei dati nel file CSV
with open('dati.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Cognome", "Età", "Altezza"])
    writer.writerow([nome, cognome, eta, altezza])

# Funzione per leggere il file CSV e generare un file HTML
def csv_to_html(csv_file, html_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)

    with open(html_file, mode='w') as file:
        file.write('<html>\n<head>\n<title>Tabella CSV</title>\n</head>\n<body>\n')
        file.write('<table border="1">\n')
        file.write('<tr>' + ''.join(f'<th>{header}</th>' for header in headers) + '</tr>\n')
        for row in rows:
            file.write('<tr>' + ''.join(f'<td>{cell}</td>' for cell in row) + '</tr>\n')
        file.write('</table>\n')
        file.write('</body>\n</html>')

# Generazione del file HTML
csv_to_html('dati.csv', 'dati.html')