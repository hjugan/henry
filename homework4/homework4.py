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

new_list = fav_foods[0:6:5]
print(new_list)

for i in range(len(fav_foods)):
    if fav_foods[i] == "potato":
        print("A potato!")
    else:
        print("No potato!")

numbers = list(range(21))

def get_first_15(list):
  return list[:15]

def get_every_5th(list):
  return list[::5]

def reverse_and_stride(list):
  reversed_list = list[::-1]
  return reversed_list[::3]

print(get_first_15(numbers))
print(get_every_5th(numbers))
print(reverse_and_stride(numbers))


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

def create_grid():
  grid = []
  number = 1
  for _ in range(5):
    row = []
    for _ in range(5):
      row.append(number)
      number += 1
    grid.append(row)
  return grid

def replace_multiples_of_three(grid):
  new_grid = []
  for row in grid:
    new_row = []
    for number in row:
      if number % 3 == 0:
        new_row.append('?')
      else:
        new_row.append(number)
    new_grid.append(new_row)
  return new_grid

def sum_numbers(grid):

  total_sum = 0
  for row in grid:
    for element in row:
      if element != '?':
        total_sum += element
  return total_sum

grid = create_grid()
print(create_grid())
question_mark_grid = replace_multiples_of_three(grid)
print(question_mark_grid)

"""
Traceback (most recent call last):
  File "/Users/hjugan/Desktop/School/2025/Fall/ASTRO 98/Python_DeCal_fa25/henry/homework4/homework4.py", line 111, in <module>
    print(replace_multiples_of_three(grid))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/hjugan/Desktop/School/2025/Fall/ASTRO 98/Python_DeCal_fa25/henry/homework4/homework4.py", line 90, in replace_multiples_of_three
    for row in grid:
TypeError: 'function' object is not iterable

I couldnt figure out how to print my functions because I couldnt pass the variable from create_grid into the other functions

I FORGOT THE FREAKING () AFTER CREATE_GRID WHEN I CALLED THE FUNCTION WHYYYYY CRUEL WORLDDDDDD

"""


ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

print(ages)

for name, age in ages.items():
  print(f"{name} is {age} years old.")

  