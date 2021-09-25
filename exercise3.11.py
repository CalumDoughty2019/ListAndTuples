

#1
#list(range(10, 0, -2)) ##start, stop, step
#[10, 8, 6, 4, 2]

#2
print()
print("question 2")
import turtle
tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
print(tess.color())
print(alex.color())
#it creates 2 pointers to the same turtle instance?
#so changing colour of one changes the colour of that instance (both pointers)

#3
print()
print("question 3")
a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a)
print(b)

#4
print()
print("question 4")
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
#print("Test 1: {0}".format(this == that))
that = this
print(this)
print(that)
print("Test 2: {0}".format(this is that))
# when we say that = this, we are changing that to point to the instance of this. If we change to this == that for test 1 we will see that it is true, but "is" means instance
