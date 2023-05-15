baris = int(input("masukan jumlah baris: "))
kolom = int(input("masukan jumlah kolom: "))
symbol = input("masukan symbol *: ")

for x in range(baris):
    for y in range(kolom):
        print(symbol, end="")
        print()