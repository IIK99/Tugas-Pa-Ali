Menu = {
    "Mie Ayam":15000,
    "Mie Ayam Bakso":18000,
    "Mie Bakso":13000,
    "Air Putih":3000,
    "Jus Mangga":7000,
    "Jus Alpukat":10000,
}
print("================== Daftar Menu =====================")
for i in Menu:
    print("Daftar Menu : ", i,"\t harga : ",Menu[i])
print("Pembelian di atas Rp.50.000,- mendapatkan diskon 10%")
print("====================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * Menu[beli]

if bayar > 50000:
    diskon = bayar*10/100
    total = bayar - diskon
else:
    total = bayar

print("\n=============== Detail pembayaran ==================")
print("Menu yang dipesan        :", beli)
print("Jumlah yang dipesan      :", jumlah)
print("Total biaya              :", bayar)
print("Total yang harus dibayar :", total)
print("================== Terimakasih =====================")