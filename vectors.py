import sys
import math

### TEST FUNCTION
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

### TEST SUITE
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    #5
    print()
    print("add_vectors")
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    #6
    print()
    print("scalar_mult")
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    #7
    print()
    print("dot_product")
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    #8
    print()
    print("cross_product")
    test(cross_product([1, 2, 1], [1, 4, 3]) == [2, -2, 2])
    #9
    print()
    print("singalong")
    test(singalong("The rain in spain") == "TheThe rain in spainrainThe rain in spaininThe rain in spainspain")
    #10
    print()
    print("replace")
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
    #11
    print()
    print("swap")


## WORKING
#5
def add_vectors(u, v):
    if(len(u) != len(v)):
        return -1
    i = 0
    new_list = []
    while i < len(u):
        t = u[i] + v[i]
        new_list.append(t)
        i = i + 1
    return new_list

#6
def scalar_mult(s, v):
    new_list = []
    i = 0
    while i < len(v):
        t = s * v[i]
        new_list.append(t)
        i = i + 1
    return new_list

#7
def dot_product(u, v):
    temp_list = []
    i = 0
    while i < len(v):
        t = u[i] * v[i]
        temp_list.append(t)
        i = i + 1
    i = 0
    p = 0
    while i < len(temp_list):
        p = p + temp_list[i]
        i = i + 1
    return p

#8
def cross_product(u, v):
    c = [u[1] * v[2] - u[2] * v[1],
         u[2] * v[0] - u[0] * v[2],
         u[0] * v[1] - u[1] * v[0]]
    return c

#9
def singalong(song):
    #song = "The rain in spain"
    print(song)
    print(song.split())
    print(song.join(song.split()))
    return song.join(song.split())
#at top of commandline
#difference is it joins the full "song" varible to the end of each split word (TheThe rain in spainrainThe rain in spaininThe rain in spainspain)

#10
def replace(s, old, new):
    if str.find(s, old):
        s = s.replace(old, new)
    return s

#11
print()
def swap(x, y):  # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
##still using local variables. I would need to change the names




test_suite()