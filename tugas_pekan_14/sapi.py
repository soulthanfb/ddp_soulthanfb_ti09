from animal import *
class sapi(animal):
#ciri-ciri
    spesies = ""
    mamalia = ""

    def __init__(self, nama, makanan, hidup, berkembangBiak, manfaat, spesies, mamalia):
        super().__init__(nama, makanan, hidup, berkembangBiak, manfaat)
        self.spesies = spesies
        self.mamalia = mamalia
# Spesies hewan
    def printSpesies(self):
        print("\n~~~ Data", self.nama, "~~~",
              "\nNama Binatang \t :",self.nama,
              "\nJenis Makanan \t :",self.makanan,
              "\nTempat Tinggal \t :", self.hidup,
              "\nReproduksi \t :", self.berkembangBiak,
              "\nManfaat \t :",self.manfaat,
              "\nSpesies \t :",self.spesies,
              "\nKeunikan \t :",self.mamalia)


              
            