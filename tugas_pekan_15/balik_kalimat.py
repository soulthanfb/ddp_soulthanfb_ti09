#urutan terbalik
balik_kalimat1 = ["saya", "mahasiswa", "Nurul", "Fikri"]
balik_kalimat2 = []
balik_kalimat3 = ["saya", "prodi", "Teknik", "Informatika"]
balik_kalimat4 = []
balik_kalimat5 = ["Pemrograman", "Dasar", "menyenangkan"]
balik_kalimat6 = []
def Reversed(balik_kalimat1, balik_kalimat2):
    for i in range(len(balik_kalimat1)):
        reversed_i = len(balik_kalimat1) -1 - i
        balik_kalimat2.append(balik_kalimat1[reversed_i])

def Reversed(balik_kalimat3, balik_kalimat4):
    for i in range(len(balik_kalimat3)):
        reversed_i = len(balik_kalimat3) -1 - i
        balik_kalimat4.append(balik_kalimat3[reversed_i])

def Reversed(balik_kalimat5, balik_kalimat6):
    for i in range(len(balik_kalimat5)):
        reversed_i = len(balik_kalimat5) -1 - i
        balik_kalimat6.append(balik_kalimat5[reversed_i])


Reversed(balik_kalimat1, balik_kalimat2)
print(f"Hasil sebelum = \n{balik_kalimat1}") 
print(f"Hasil sesudah = \n{balik_kalimat2}")
print("=========================================")

Reversed(balik_kalimat3, balik_kalimat4)
print(f"Hasil sebelum = \n{balik_kalimat3}") 
print(f"Hasil sesudah = \n{balik_kalimat4}")
print("=========================================")

Reversed(balik_kalimat5, balik_kalimat6)
print(f"Hasil sebelum = \n{balik_kalimat5}") 
print(f"Hasil sesudah = \n{balik_kalimat6}")