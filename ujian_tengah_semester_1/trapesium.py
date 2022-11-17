# program menghitung luas dan keliling trapesium
#Input
a = int(input("Masukkan Alas A = "))
b = int(input("Masukkan Alas B = "))
c = int(input("Masukkan Alas C = "))
d = int(input("Masukkan Alas D = "))
t = int(input("Masukkan Tinggi Trapesium= "))

#Proses
luas_trapesium = 1/2 * ( a+b ) * t
keliling_trapesium = a+b+c+d

#Output
print("Hasil luas trapesium adalah = ", luas_trapesium)
print("Hasil keliling trapesium adalah = ", keliling_trapesium)