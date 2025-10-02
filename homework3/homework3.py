# File: homework3.py

name =  "Henry"

def say_goodbye(name):
	print("Goodbye,", name)

say_goodbye(name)

radius = 5
def area_of_circle(radius):
	area = 3.14 * radius**2
	print(area)

area_of_circle(radius)

a = 12
b = 9

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

temps = [20, 24, 19, 24, 17, 18, 26]

high = max(temps)
low = min(temps)
xtremes = (high, low)
print(xtremes)

monday = 1
tuesday = 2 
wednesday = 3
thursday = 4
friday = 5
saturday = 6
sunday = 7

def check_day(day):
	if day >= 6:
		print("It's the weekend!")
	else:
		print("It's a weekday")


check_day(wednesday)

distance = 45
gallons = 11
def mpg(a, b):
	c = a / b
	return(c)

mpg(distance, gallons)



def secret_code(number):
	if number < 10:
		return number
	last_digit = number % 10

	rest_of_number = number // 10
	num_digits = len(str(rest_of_number))
	encrypted_number = last_digit * (10**num_digits) + rest_of_number
  
	return encrypted_number

num = 78978
encrypted_num = secret_code(num)
secret_code(num)
print(num)
print(encrypted_num)

x = 5
y = 3
def exponents(x, y):
	a  = 1
	for i in range(y):
		a *= x
	print(a)

exponents(x, y)

list_a = [1, 18, 34, 13, 1224, 235, 43, 2, 6]

def min_num(list):
	min = list[0]
	for i in list:
		if i < min:
			min = i
	print(min)

min_num(list_a)

def max_num(list):
	max = list[0]
	for i in list:
		if i > max:
			max = i
	print(max)

max_num(list_a)

def while_max(list):
	max = list[0]
	i = 1
	while i < len(list):
		a = list[i]
		if a > max:
			max = a
		i += 1
	return max

def while_min(list):
	min = list[0]
	i = 1
	
	while i < len(list):
		if list[i] < min:
			min = list[i]
		i += 1
	return min

print(while_max(list_a))
print(while_min(list_a))

number = 37912

def sum(n):
	string_n = str(n)
	sum = 0
	for i in string_n:
		sum += int(i)
	print(sum)


sum(number)