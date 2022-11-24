baris = int(input('Jumlah baris yang ingin diulang: '))
i = 1
for i in range (baris):
    for j in range (i+1):
        print ('*', end='')
    print ('')