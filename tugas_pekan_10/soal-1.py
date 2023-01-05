<<<<<<< HEAD
#nama siswa yang lulus
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def lulus_saja(hasil_akhir):
    for lulus_saja in hasil_akhir:
        if(lulus_saja['nilai'] > 65):
            print(f"Hasilnya = \n{lulus_saja}")

=======
#nama siswa yang lulus
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def lulus_saja(hasil_akhir):
    for lulus_saja in hasil_akhir:
        if(lulus_saja['nilai'] > 65):
            print(f"Hasilnya = \n{lulus_saja}")

>>>>>>> 7a3962629709e01c638a5ccc5de7a2655e5d8c24
lulus_saja(hasil_akhir)