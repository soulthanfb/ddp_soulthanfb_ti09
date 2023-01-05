from animal import *
class ayam(animal):
#ciri-ciri
    pertahanan = ""
    keunikan = ""

    def __init__(self, nama, makanan, hidup, berkembangBiak, manfaat, pertahanan, keunikan):
        super().__init__(nama, makanan, hidup, berkembangBiak, manfaat)
        self.pertahanan = pertahanan
        self.keunikan = keunikan
#Bentuk Pertahanan Diri dan Keunikan
    def printPertahanan(self):
        print("\n~~~ Data", self.nama, "~~~",
              "\nNama Binatang \t :",self.nama,
              "\nJenis Makanan \t :",self.makanan,
              "\nTempat Tinggal \t :", self.hidup,
              "\nReproduksi \t :", self.berkembangBiak,
              "\nManfaat \t :",self.manfaat,
              "\nPertahanan \t :",self.pertahanan,
              "\nKeunikan \t :",self.keunikan)


            