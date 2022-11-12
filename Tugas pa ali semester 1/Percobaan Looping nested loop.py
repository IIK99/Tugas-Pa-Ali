from tkinter import N


baris = int(input("masukan jumlah baris "))
kolom = int(input("masukan jumlah kolom "))

for b in range(1, baris+1):
    for k in range(1, kolom-b+2):
        print("*", end="")

        print("\n")
