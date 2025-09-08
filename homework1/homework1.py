#File: homework1.py

# ---Variables and Data Types ---

a = 10 
print(a)
print(type(a)) #a is an integer, a whole number w/ no decimals

b = 1.5
print(b)
print(type(b)) #b is a float, a number with decimal places

c = 3j
print(c)
print(type(c)) #c is complex, these data types store complex numbers following the form a+bj where j represents the imaginary unit

d = "hello"
print(d)
print(type(d))# d is a string, a string contains text

e = [1, 2, 3]
print(e)
print(type(e)) #e is a list, lists store values that can be called upon by referencing the list and the position of the value within the list. You can add/delete items from lists

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dict, associates data with a "key" that allows for quick referencing

g = (1, 2)
print(g)
print(type(g)) #g is a tuple, tuples are like lists, but the data cannot be changed once you declare the tuple

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list, refer to explanation in e (this list is a bit different because it stores strings not integers)

i = True
print(i)
print(type(i)) #i is a bool, boolean data types are used for structures that are either true or false

j = None
print(j)
print(type(j)) #j is none, just means there is no data stored within the variable

k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list, refer to explanation above

l = str(14)
print(l)
print(type(l)) #l is a string, it may print integers in this case, but they are stored as characters

m = 1e4
print(m)
print(type(m)) #m is a float, but it is in scientific notation!

"""
Questions:

1. How many different data types did you find?
    9

2. List all the data types you found.
    string, list,bool, float, integer, dict, tuple, complex, none

3. What variables have the same data types?
    b&m, h&e, d&l

4. What was the data type of l? Why is it not an integer? What does str() do?
    l is a string. It takes the argument and converts it into a string

5. Look up one more data type not given above. Repeat the same procedure.
    5 is provided outside the comments.

"""

n = {1,2,3}

o = frozenset(n)
print(o)
print(type(o)) #o is a frozenset, it takes a set and makes it so that the elements cannot be changed, added, or deleted

print(10 > 9) #True, 10 is greater than 9
print(10 == 9) #false, 10 does not equal 9
print(10 <= 9) # false, 10 is greater than 9

bool_list = [bool("abc"), bool(123), bool(["apple", "cherry", "banana"]), bool(True), bool(False), bool(0), bool(""), bool(" "), bool(()), bool([]), bool({}), bool(True and False), bool(True and True), bool(False and False), bool(True or False), bool(True or True), bool(False or False), bool(not(False)), bool(not(True))]

print(bool_list)

"""
In order of command: True (this is because there is an input to the bool operator with non-empty data) <-let explanation in () = explanation1
True (explanation1)
True(explanation1)
True(true is already a boolean data type, so when you pass it through the boolean function it will just return the value it already has) 
False(same explanation as above)
False(the input given is an empty data type so it returns false)
False(Same explanation as above), True, False, False, False, False, True, False, True, True, False, True, False
"""