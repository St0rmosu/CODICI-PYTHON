import os

# cognome_nome.py


def read_cabins(file_path):
    cabins = []
    with open(file_path, 'r') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            cabins.append(dict(zip(headers, line.strip().split(','))))
    return cabins

def navigate_cabins(cabins):
    for i, cabin in enumerate(cabins):
        print(f"Cabin {i+1}:")
        for key, value in cabin.items():
            print(f"{key}: {value}")
        print()

def export_navigation(cabins, output_file):
    with open(output_file, 'w') as file:
        for i, cabin in enumerate(cabins):
            file.write(f"Cabin {i+1}:\n")
            for key, value in cabin.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

def cabins_to_html(cabins, output_file):
    with open(output_file, 'w') as file:
        file.write("<html><body><table border='1'>\n")
        headers = cabins[0].keys()
        file.write("<tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr>\n")
        for cabin in cabins:
            file.write("<tr>" + "".join(f"<td>{value}</td>" for value in cabin.values()) + "</tr>\n")
        file.write("</table></body></html>")

def main():
    file_path = 'cabine_nave.txt'
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    cabins = read_cabins(file_path)
    navigate_cabins(cabins)

    output_file = input("Enter the name of the output file (with .txt extension): ")
    export_navigation(cabins, output_file)

    html_output_file = input("Enter the name of the HTML output file (with .html extension): ")
    cabins_to_html(cabins, html_output_file)

if __name__ == "__main__":
    main()