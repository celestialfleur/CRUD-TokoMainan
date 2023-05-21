import os
import time
import random

uang = 5000000
admin = (random.getrandbits(8))
menu = {
    "Gundam":350000,
    "Hotweels":50000,
    "Barbie":100000,
    "Boneka":120000,
    "Nerf-gun":250000,
    "Aeromodeling":750000
}
print("Uang Kamu Ada 5.000.000")
print("====== Toko Mainan Apik ======")
for i in menu:
    print("Daftar Barang : ", i,"\t Harga : ",menu[i])
print("Pembelian di atas Rp1.000.000,- Mendapatkan Diskon 15%")
print("========================================")
beli = input("Pilih Barang : ")
jumlah = int(input("Jumlah Barang : "))
bayar = jumlah * menu[beli] + admin

if bayar > 5000000:
    diskon = bayar*15/100
    total = bayar - diskon + admin
else:
    total = bayar + admin
    uang = uang - total - admin
if total < uang:
    uang = uang - total - admin
print("=========== Struk Pembayaran ===========")
print("Menu yang di beli        : ",beli)
print("Jumlah yang di pesan     : ",jumlah)
print("Biaya Admin              :",admin)
print("Total biaya              : ",bayar)
print("Total yang harus dibayar : ",total)
print("========================================")
print("Uang kamu tersisa : ",uang)
print("====== THANK YOU SUDAH BERBELANJA ======")
if total > uang:
    os.system('cls')
    time.sleep(2)
    print("Kamu gagal membeli karena uangmu kurang!!")