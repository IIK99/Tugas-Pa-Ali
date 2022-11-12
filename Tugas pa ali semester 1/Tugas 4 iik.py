from tkinter import N


print("selamat Datang di FishColony\n")

Kategori_Air= input('Masukan Kategori Air[Tawar/Payau/Asin]=')
if Kategori_Air=='Tawar' or Kategori_Air=='tawar':
    KategoriAir='Air Tawar'
    JenisIkan='Ikan Mujair,Ikan Mas, Ikan Gabus'
elif Kategori_Air=='Payau' or Kategori_Air=='payau':
    KategoriAir='Air Payau'
    JenisIkan="Ikan Bandeng, Ikan Bawal, Ikan Mudskipper"
else :
    KategoriAir='Air Asin'
    JenisIkan='Ikan Buntal, Ikan Pari, Ikan Hiu'

print('Kategori Air         =',KategoriAir)
print('Jenis-jenis Ikan     =', JenisIkan)
Jenis_Ikan = input('Masukan Jenis Ikan  = ')
if Jenis_Ikan=='mujair' or Jenis_Ikan=='Ikan Mujair':
    JenisIkan='Ikan Mujair'
    Tersedia=1000
elif Jenis_Ikan=='mas' or Jenis_Ikan=='Ikan Mas' :
    JenisIkan= 'Ikan Mas'
    Tersedia=750
elif Jenis_Ikan=='gabus' or Jenis_Ikan=='Ikan Gabus' :
    JenisIkan='Ikan Gabus'
    Tersedia=500
elif Jenis_Ikan=='bandeng' or Jenis_Ikan=='Ikan Bandeng' :
    JenisIkan='Ikan Bandeng'
    Tersedia=2000
elif Jenis_Ikan=='bawal' or Jenis_Ikan=='Ikan Bawal' :
    JenisIkan='Ikan Bawal'
    Tersedia=400
elif Jenis_Ikan=='mudskipper' or Jenis_Ikan=='Ikan Mudskipper' :
    JenisIkan='Ikan Mudskipper'
    Tesedia=5000
elif Jenis_Ikan=='buntal' or Jenis_Ikan=='Ikan Buntal' :
    JenisIkan='Ikan Buntal'
    Tersedia=670
elif Jenis_Ikan=='pari' or Jenis_Ikan=='Ikan Pari':
    JenisIkan='Ikan Pari'
    Tersedia=300
else:
    Jenis_Ikan=='hiu' or Jenis_Ikan=='Ikan Hiu'
    JenisIkan='Ikan Hiu'
    Tersedia=225
print('Kategori Air         =',KategoriAir)
print('Jenis Ikan           =',JenisIkan)
print('Jumlah Stok          =', Tersedia)
print('\n')
print('Terima kasih telah datang ke FishColony')