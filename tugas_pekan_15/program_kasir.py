from kasir import *

kantin = Kasir()

print(f'='*40)
konsumen1 = Konsumen('Soulthan Fadlillah Bagus', 150000)
konsumen1.pesan(kantin, {'ayam goreng': 2, 'kopi': 1})

print(f'='*40)
konsumen2 = Konsumen('Maleek Fatahilah Bagus', 150000)
konsumen2.pesan(kantin, {'nasi goreng': 1, 'teh manis': 2, 'sate': 1})

print(f'='*40)
konsumen3 = Konsumen('Akhyar', 150000)
konsumen3.pesan(kantin, {'nasi goreng': 1, 'teh manis': 2, 'sate': 1})