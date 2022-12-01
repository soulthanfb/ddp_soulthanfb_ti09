def kuliah():
    cuaca = input("Jika cuaca hari ini: ")
    def status():
        if(cuaca == "hujan"):
            berangkat = "Maka berangkat naik gocar"
        elif(cuaca == "sejuk"):
            berangkat = "Maka berangkat naik motor"
        return berangkat
    print("Jika kondisi cuaca %s" ": %s" %(cuaca,status()))
kuliah()
