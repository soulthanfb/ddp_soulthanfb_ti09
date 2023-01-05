from animal import *
class kambing(animal):
#ciri-ciri
    jenis = ""
    bertanduk = ""

    def __init__(self, nama, makanan, hidup, berkembangBiak, manfaat, jenis, bertanduk):
        super().__init__(nama, makanan, hidup, berkembangBiak, manfaat)
        self.jenis = jenis
        self.bertanduk = bertanduk 
#Jenis Kambing
    def printJenis(self):
        print("\n~~~ Data", self.nama, "~~~",
              "\nNama Binatang \t :",self.nama,
              "\nJenis Makanan \t :",self.makanan,
              "\nTempat Tinggal \t :", self.hidup,
              "\nReproduksi \t :", self.berkembangBiak,
              "\nManfaat \t :",self.manfaat,
              "\nJenis Kelamin\t :",self.jenis,
              "\nBertanduk \t :",self.bertanduk)

            