class animal:
    nama = ""
    makanan = ""
    hidup = ""
    berkembangBiak = ""
    manfaat = ""

    def __init__(self, nama, makanan, hidup, berkembangBiak, manfaat):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
        self.manfaat = manfaat

    def printAnimal(self):
        print("\n~~~ Data", self.nama, "~~~~",
              "\nNama Binatang \t :",self.nama,
              "\nJenis Makanan \t :",self.makanan,
              "\nTempat Tinggal \t :", self.hidup,
              "\nReproduksi \t :", self.berkembangBiak,
              "\nManfaat \t :",self.manfaat)



