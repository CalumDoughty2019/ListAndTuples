import sys

horsemen = ["war", "famine", "pestilence", "death", "kkk"]
i = 0
while i < 4:
    print(horsemen[i])
    i = i+1
print()
#sys.exit(0)

i = 0
while i < len(horsemen):
    print(horsemen[i])
    i = i+1
print()
#sys.exit(0)

listOne = [1, 2, 3, 4]
listTwo = [1.5, 2.5, 3.5, 4.5]
listThree = ['a', 'b', 'c', 'd']
bigList = [listOne, listTwo, listThree]
print(bigList)
#sys.exit(0)

list4 = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(len(list4))
print(list4)
#sys.exit(0)
