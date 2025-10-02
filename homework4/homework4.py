fav_foods = ["pho", "burrito", "sushi", "thai curry", "bahn mi"]

print(fav_foods[1])
print(fav_foods[-1])

fav_foods.append("ramen")
fav_foods.insert(0, "apple")
print(fav_foods)
"""
  File "/Users/hjugan/Desktop/School/2025/Fall/ASTRO 98/Python_DeCal_fa25/henry/homework4/homework4.py", line 7
    fav_foods.insert("apple":0)
                            ^
SyntaxError: invalid syntax

I wrote fav_foods.insert("apple":0) but the insert function takes the index first and then the string second
"""
del fav_foods[2]
print(len(fav_foods))

for i in range(len(fav_foods)):

    print(fav_foods[i].upper())

"""
  File "/Users/hjugan/Desktop/School/2025/Fall/ASTRO 98/Python_DeCal_fa25/henry/homework4/homework4.py", line 22, in <module>
    print(fav_foods.upper(i))
          ^^^^^^^^^^^^^^^
    I had my index as a parameter inside of upper when it should have been inside of fav_foods
AttributeError: 'list' object has no attribute 'upper'
"""

# new_list = fav_foods[0:6:5]
# print(new_list)

# for i in range(len(fav_foods)):
#     if fav_foods[i] == "potato":
#         print("A potato!")
#     else:
#         print("No potato!")

# numbers = list(range(21))
# print(numbers)

# def get_first_15(numbers):
#     global first_15
#     first_15 = numbers[:15]
#     return first_15

# def every_5th(first_15):
#     global every_5th
#     every_5th = first_15[0:15:5]
#     return every_5th

# def reverse(every_5th):
#     global rev
#     rev = every_5th
#     return rev

# print(get_first_15(numbers))
# print(every_5th(first_15))
# print(reverse(rev))

"""
  File "/Users/hjugan/Desktop/School/2025/Fall/ASTRO 98/Python_DeCal_fa25/henry/homework4/homework4.py", line 53, in <module>
    print(every_5th(first_15))
                    ^^^^^^^^
NameError: name 'first_15' is not defined
I didn't make a global variable named first 15
My code was: 
def get_first_15(numbers):
    first_15 = numbers[:15]
    return first_15
"""


numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2])

print(numbers[1][1])
numbers.append([10, 11, 12])
print(numbers)

def sum_numbers(numbers):
    for sublist in numbers:
        for i in sublist:
            print(i)

sum_numbers(numbers)

def create_five_x_five(five_x_five):
    five_x_five = []
    counter = 1
    for row_num in range(5):
        new_row = []
        for col_num in range(5):
            new_row.append(counter)
            counter += 1
        five_x_five.append(new_row)

    return five_x_five



def three_to_q(five_x_five):
    new_grid
    new_grid = []
    for row in five_x_five:
        new_row = []
        for number in five_x_five:
            if number % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(number)
        new_grid.append(new_row)
    return new_grid
    
grid = []
grid = create_five_x_five(grid)
new_grid = three_to_q(grid)
print("Original Grid:")
for row in grid:
    print(row)

print("\nGrid with Replacements:")
for row in new_grid:
    print(row)


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages.["Katie"])
