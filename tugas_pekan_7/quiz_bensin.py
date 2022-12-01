#program pemesanan bensin
#Declaring/Menyatakan
pLite = 10000
pMax  =  14000
pTurbo  =  17000

jTempuhPLite  =  12
jTempuhPMax  =  13
jTempuhPTurbo  =  13.5

jakarta  =  20
bekasi  =  35,7
depok  =  5
tangerang  =  99
bogor  =  120.6

#Memasukan
NamaKendaraan = input("Nama Kendaraan? ")
JenisBensin = input("Jenis Bensin? ")
KotaDiTuju = input("Kota Yang Dituju? ")

#Proses
if KotaDiTuju == "jakarta":
    Jarak = 20
elif KotaDiTuju == "bekasi":
    Jarak = 35.7
elif KotaDiTuju == "depok":
    Jarak = 5
elif KotaDiTuju == "tangerang":
    Jarak = 99
elif KotaDiTuju == "bogor":
    Jarak = 120.6
if JenisBensin == "pertalite":
    Harga = 10000
    JarakTempuh = 12
elif JenisBensin == "pertamax":
    Harga = 14000
    JarakTempuh = 13
elif JenisBensin == "pertamax Turbo":
    Harga = 17000
    JarakTempuh = 13.5

#pembulatan
PemakaianBensin = round(JarakTempuh * Jarak)
HargaBensin = round(Harga * Jarak)

#output
print("----------------------------------")
print("Nama Kendaraan = ",NamaKendaraan)
print("Jenis Bensin = ",JenisBensin)
print("Kota Yang Dituju = ",KotaDiTuju)
print("Pemakaian Bensin = ",PemakaianBensin,"L")
print("Total Harga Bensin = ", "Rp",HargaBensin)