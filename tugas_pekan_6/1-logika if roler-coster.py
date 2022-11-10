#Buat Program mnggunakan logika if untuk roler coster dengan tinggi min 90 cm boleh main dan dibawah 90 tidak boleh main
#Input
nama = input("Masukkan nama Anda? ")
umur = input("Masukkan umur Anda? ")
tinggi = int(input("Masukkan tinggi Anda? "))

#Proses
if tinggi > 89:
    ket = "Boleh bermain Roler Coster"
else :
    ket = "Tidak boleh bermain Roler Coster"

#Output
print("Nama saya ",nama)
print("Umur saya ",umur,"Thn")
print("Tinggi saya ",tinggi,"cm")
print("Kamu ",ket)