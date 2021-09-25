import sys

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
#sys.exit(0)

d = [0] * 4
print(d)
e = [1, 2, 3] * 3
print(e)
#sys.exit(0)

list5 = ['a', 'b', 'c', 'd', 'e', 'f']
print(list5[1:3])
print(list5[:4])
print(list5[3:])
#sys.exit(0)

#change value (mutable)
fruit = ["banana", "apple", "quince"]
fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)
#sys.exit(0)

#insert into list
list6 = ['a', 'd', 'f']
list6[1:1] = ['b', 'c']
print(list6)
list6 = ['a', 'd', 'f']
list6[0:1] = ['b', 'c']
print(list6)