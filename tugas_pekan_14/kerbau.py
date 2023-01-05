from animal import *
class kerbau(animal):
#ciri-ciri
    warna = ""
    keunikan = ""

    def __init__(self, nama, makanan, hidup, berkembangBiak, manfaat, warna, keunikan):
        super().__init__(nama, makanan, hidup, berkembangBiak, manfaat)
        self.warna = warna
        self.keunikan = keunikan
#Warna Hewan
    def printWarna(self):
        print("\n~~~ Data", self.nama, "~~~",
              "\nNama Binatang \t :",self.nama,
              "\nJenis Makanan \t :",self.makanan,
              "\nTempat Tinggal \t :", self.hidup,
              "\nReproduksi \t :", self.berkembangBiak,
              "\nManfaat \t :",self.manfaat,
              "\nWarna Kerbau\t :",self.warna,
              "\nKeunikan \t :",self.keunikan)


            