print("Selamat Datang di Hunger Ranger!")
print("Silahkan Login untuk masuk ke aplikasi!")
Data_UserID = ['BreadsosIndonesia']
Data_Password = ["#indonesiaantifoodwaste"]

p = False
while p == False :
    UserID = input("Masukkan User ID       :")
    p = UserID in Data_UserID
    if p == True :
        q = Data_UserID.index(UserID)
        r = False
        while r == False :
            Pass = input("Masukkan password      :")
            r = Pass == Data_Password[q]
            if r == True :
                break
            else:print("Password anda salah, silahkan coba lagi!")
    else:print("Maaf, User tidak terdaftar.")    
print("Login sukses, selamat datang di Hunger Ranger!.")