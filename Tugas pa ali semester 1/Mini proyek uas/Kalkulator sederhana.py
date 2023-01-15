# Proyek sederhana
# Kalkulator sederhana

print(20*"=")
print("Kalkulator sederhana")
print(20*"=" + "\n")

Angka_1 = float(input("Masukan angka pertama = "))
Operator = input("Pilih operator (+,-,x,/) : ")
Angka_2 = float(input("Masukan angka kedua = "))

Lanjut = True
if Operator == "+":
    Hasil = Angka_1 + Angka_2
    print(f"Hasilnya adalah = {Hasil}")

elif Operator == "-":
    Hasil = Angka_1 - Angka_2
    print(f"Hasilnya adalah = {Hasil}")
    
elif Operator == "x":
    Hasil = Angka_1 * Angka_2
    print(f"Hasilnya adalah = {Hasil}")
    
elif Operator == "/":
    Hasil = Angka_1 / Angka_2
    print(f"Hasilnya adalah = {Hasil}")
    
else:
    print("Tolong masukan input operator yang bener dong! Saya gak ngarti setting proggramnya")

    print("\n")


Akhir = input("Lanjut (y/n)? ")
while Lanjut:
        if Akhir == "n":
            break
    
print("Proggram selesai")