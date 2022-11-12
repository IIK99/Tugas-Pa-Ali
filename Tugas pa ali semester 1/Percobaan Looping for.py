listkelas = ["A1", "A2", "B1", "C1"]

salah = True

i = 0

while salah:
    jawaban = input("Masukan kelas anda: ")

    for item in listkelas:
        if jawaban == item:
            salah = False

    if salah:
        i+=1
        print("Input anda salah. Anda sudah mencoba sebanyak "+str(i)+" kali")

print("Input anda benar")
