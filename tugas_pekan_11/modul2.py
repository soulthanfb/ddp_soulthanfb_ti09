# kelopok fungsi
import math

def lingkaran(r):
  phi = 22 / 7
  luas = r * r * phi
  print("Luas lingkaran dengan jari-jari", r, "adalah", luas)

def persegi(sisi):
  luas = sisi * sisi
  print("Luas persegi dengan sisi", sisi, "adalah", luas)
  
def persegiPanjang(p, l):
  luas = p * l
  print("Luas persegi panjang dengan panjang", p, "dan lebar", l, "adalah", luas)

def segitiga(a, t):
  luas = (a * t) / 2
  print("Luas segitiga dengan alas", a, "dan tinggi", t, "adalah", luas)

def belahKetupat(d1, d2):
  luas = (d1 * d2) / 2
  print("Luas belah ketupat dengan diagonal satu", d1, "dan diagonal dua", d2, "adalah", luas)

def jajargenjang(a, t):
  luas = a * t
  print("Luas Jajargenjang dengan alas", a, "dan tinggi", t, "adalah", luas)

def trapesium(a, b, t):
  luas = 1/2 / (a + b * t)
  print("Luas Trapesium dengan jumlah panjang garis sejajar", a+b , "dan tinggi", t, "adalah", luas)