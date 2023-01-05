from gempa_bumi import *
# Object
gempa1 = gempa_bumi("Banten", 1.2)
gempa2 = gempa_bumi("Pala", 6.1)
gempa3 = gempa_bumi("Cianjur", 5.6)
gempa4 = gempa_bumi("Jayapura", 3.3)
gempa5 = gempa_bumi("Garut", 4.0)

gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()