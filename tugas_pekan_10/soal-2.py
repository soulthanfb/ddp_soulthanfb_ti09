<<<<<<< HEAD
#urutan terbalik nama buah
listA = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
listB = []
def Reversed(listA, listB):
    for i in range(len(listA)):
        reversed_i = len(listA) -1 - i
        listB.append(listA[reversed_i])

Reversed(listA, listB)
print(f"Hasil sebelum = \n{listA}") 
=======
#urutan terbalik nama buah
listA = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
listB = []
def Reversed(listA, listB):
    for i in range(len(listA)):
        reversed_i = len(listA) -1 - i
        listB.append(listA[reversed_i])

Reversed(listA, listB)
print(f"Hasil sebelum = \n{listA}") 
>>>>>>> 7a3962629709e01c638a5ccc5de7a2655e5d8c24
print(f"Hasil sesudah = \n{listB}")