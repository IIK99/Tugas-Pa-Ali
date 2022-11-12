salah = True

i = 0

while salah:

    jawaban = input("Masukan password: ")

    if jawaban == "kelas_malam":
        break
    else:
        i+=1
        print("Password anda salah. Anda sudah mencoba sebanyak: "+str(i))

print("Password anda benar")
