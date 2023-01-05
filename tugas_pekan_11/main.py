# memanggil dan menjalankan modul2
print("====================Modul Bangun Datar====================")
import modul2 as hasil
hasil.lingkaran(22)
hasil.persegi(8)
hasil.persegiPanjang(9, 3)
hasil.segitiga(7, 7)
hasil.belahKetupat(5, 5)
hasil.jajargenjang(15, 6)
hasil.trapesium(8, 3, 6)

print(" ")

#memanggil dan menjalankan modul 1
from modul1 import tambah, kurang, kali
print("=====================Modul Aritmatika=====================")
tambah(3, 5, 7, 8)
kurang(35, 12, 24)
kali(4, 5, 7, 9)