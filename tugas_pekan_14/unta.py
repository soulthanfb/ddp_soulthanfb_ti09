from animal import *
class unta(animal):
#ciri-ciri
    morfologi = ""
    keunikan = ""

    def __init__(self, nama, makanan, hidup, berkembangBiak, manfaat, morfologi, keunikan):
        super().__init__(nama, makanan, hidup, berkembangBiak, manfaat)
        self.morfologi = morfologi
        self.keunikan = keunikan
#Bentuk Pertahanan Diri
    def printMorfologi(self):
        print("\n~~~ Data", self.nama, "~~~",
              "\nNama Binatang \t :",self.nama,
              "\nJenis Makanan \t :",self.makanan,
              "\nTempat Tinggal \t :", self.hidup,
              "\nReproduksi \t :", self.berkembangBiak,
              "\nManfaat \t :",self.manfaat,
              "\nMorfologi  \t :",self.morfologi,
              "\nKeunikan \t :",self.keunikan)


              
            