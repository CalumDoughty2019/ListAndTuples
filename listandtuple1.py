import sys
#tuples are immutable lists

list1 = [5, 6, 7, 8]
print(type(list1))
print(list1)
#sys.exit(0)

list2 = ["spam", "bungee", "swallow"]
list3 = ["hello", 2.0, 5]
print(list1, list2, list3)
empty_list = []
print(list1, list2, list3, empty_list)
#sys.exit(0)

#lists are mutable
numbers = [17, 123]
print(numbers[0])
numbers[0] = 5500
print(numbers[0])
print(numbers[-1])
sys.exit(0)