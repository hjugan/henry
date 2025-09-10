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
False(Same explanation as above)
True(explanation1)
False(this is an empty tuple, empty data type -> false) 
False(same explanation as above except data type is a list)
False(same explanation as above except data type is a dict)
False(the and operator will return true only if both sides are true)
True(there is no logical contradiction, the and operator has two true values passed through)
False(both sides of the and operator are false)
True(The or operator will return true if at least one side of the operator is true)
True(same explanation as above)
False(same explanation as above) 
True(the not operator INVERTS the argument so false -> true)
False(same explanation as above except inverted circumstance)
"""

"""
Questions:
1. The presence of data within the data type would make the boolean operator return true
2. the first instances of false surprised me 
3. bool(not(False and False)) <- This is true because the not operator inverts the falsiness of false and false
4. bool(not(True or False))  <- the false operator inverts the truthiness of the argument True or False
"""

#   ---Arithmatic Operators---

print(10 + 5) #15, + adds
print(10 - 5) #5, - subtracts
print(2 * 4) #8, * multiplies
print(6 / 3) # 2, / divides
print(5 % 2) #1, returns the remainder when dividing the #s
print(3 ** 2) #9, ** puts the 2nd # in the exponent of the first
print(15 // 2) #7, // divides and rounds 

#   ---Comparison Operators---

print(5 == 2) #False, == compares to see if either side is equal
print(10 != 10) #False, != compares to see if either side is not equal
print(2 < 5) #True, < checks to see if left side is less than
print(12 > 5) #True, > checks to see if left side is greater than
print(5 <= 6) #True <= checks to see if left side is less than or equal to
print(1 >= 10) #False, >= checks to see if left side is greater than or equal to

#   ---Assignment Operators---

x = 5

x += 5 #adds 5 to x and then sets x = to sum
print(x)
x -= 4 #subtracts 4 from x and then sets x = to difference
print(x)
x *= 3 #multiplies x by 3 and then sets x = to product
print(x)

"""
1. What does the operator and do? Write an expression that results in True. Write an expression
that results in False.
    The and operator combines two statements and returns true if both are true and false otherwise
    bool(10==10 and True)
    bool(True and 5>11)

2. What does the operator or do? Write an expression that results in True. Write an expression
that results in False.
    The or operator connects two conditional statements and returns true if at least one of them is true
    bool(True or 5!=5)
    bool(10>11 or False)

3. What does the operator not do? Write an expression that results in True. Write an expression
that results in False

    the not operator inverts the truth of a statement
    bool(not(7!=7))
    bool(not(True))
"""

"""
More Questions:

1. What is the difference between / and //?
    / does float division and // does floor division ( does not return decimal)
2. What is the difference between % and //?
    % returns the remainder and // returns the dividend without any remainder
3. What operator would you use to calculate the remainder when dividing two numbers? Give
an example.
    you would use %
    print(10%6) <- returns 4
4. How do assignment operators work?
    assignment operators allow you to perform arithmatic on a variable and then change the variable to the newly calculated number

"""

my_string = "hello"

print(my_string)
print(my_string[0]) # prints character at 0 index
print(my_string[1]) # ^ but 1
print(my_string[2]) # ^ but 2
print(my_string[3]) # ^ but 3
print(my_string[4]) # ^ but 4
print(my_string[-1]) # goes back to the last index
print(my_string[1:3]) #slices the string, printing the characters starting at index 1 up to, but not including index3
print(my_string[0:5:2]) #slices the string from the 0th to 5th index but in increments of 2 (prints index 0,2,4)
print(len(my_string)) #prints the # of characters in the string
print(my_string + "goodbye") #adds goodbye to the end of my string
print(7 * my_string) #prints my string 7 times

#print(my_string[0:7])
#print(my_string[2:9])
name = "Oski"
print("Hello, my name is", name)

print(f"Hello, my name is {name}")
"""
Questions:

1. Define the term slicing. For which of the manipulations did you slice your string?
    Slicing extracts specific characters from a string. I sliced w/ the commands print(my_string[1:3]) and print(my_string[0:5:2]) 

2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
    This code prints the variable 'name' after the string with a space
3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
    The output to terminal looks the same
4. What is the difference between the two last print statements?
Hint: Look up f-strings.

    f-strings allow you to store variable calls within the string, making the string dynamic and able to be formatted/changed at the time of running the script

"""

"""
    ---Terminal Commands---
1. Define the command as a comment.
2. Explain how to use it.
3. Give an example of how to use it.
4. Try out the command on your terminal.

"""

#cd
# Changes directories in terminal
# cd Documents

#ls
#lists the contents of a directory
# ls 

#ls -a
# lists the files + hidden files in a directory
# ls -a

#mkdir
# makes a directory
# mkdir favorite_folder

#cat
# prints the text within a file
# cat favorite_file

#pwd
# prints the file path of the directory that you are currently in
# pwd

#cd ..
# navigates to the parent folder of your current directory
# cd ..

# cd .
# navigates to your current directory
# cd .

# cd ∼
# this takes you to the home directory
# cd ~

# cp
# copies a specified file or directory
# cp homework1.py /Users/hjugan/Desktop/
# cp homework1.py homework1_copy.py

#mv
# moves a files or directories or renames a file
# mv homework1_copy.py /Users/hjugan/Desktop/
# mv test_file.txt test_file_rename.txt

#rm (be careful with this one)
# removes a file or directory
# rm homework1.py (NOOO!!!)
# rm -r /Users/hjugan

#clear
# clears the terminal screen
# clear

#grep
# searches text within a file or directory for a string that matches the given string
# grep "hello world" homework1.py


"""
1. Look up 3 other commands not present. Define and explain how to use them on the command
line.

    1. top
        top displays all of the tasks and processes running on your computer
        top

    2. zip
        zip allows you to take files and compress them into a .zip file
        zip homework1.zip homework1.py screenshot3.png

    3. man
        man gives the "user manual" description of a command, which is cool for understanding foreign commands
        man grep



2. What is the difference between ls and ls -a?
    ls lists the contents of a file and ls -a lists ALL the contents of a file including hidden folders/files

3. What is a hidden file?
    it is a file that is not shows in a directory in order to prevent accidental deletion or altering

4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
use them on the command line.

    1. -r for the rm command
    -r does recursive removal, which means that it will remove every file in a directory and then the directory itself

    2. -f
        -f forces a command, overriding any blocks or necessary confirmations for a command

    3. -e with conditional expressions
        -e is used with conditional commands and returns true if a file/directory exists and false otherwise
"""

