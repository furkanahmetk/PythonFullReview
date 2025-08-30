import math

"""print("HELLO WORLD :D")
print("*" * 10)

x = 1
unit_price = 3"""

student_count = 1000  # int
rating = 4.99  # float
is_published = False  # boolean
course_name = "Python Programming"  # String
print(student_count)

course = "Python Programming"

message = """
Hi, John

How are you .

blah blah blah
"""

# strings
print("length of message is : ", len(message))
print(course[0], course[-1], course[0:3], course[0:], course[:4], course[:])

# escape sequences
# \" \' \\ \n
course_v2 = "Python \"Programming"
print(course_v2)

# formatted strings

first = "ali"
last = "veli"
full = first + " " + last
print(full)

full_v2 = f"{first} {last}"
print(full_v2)

# string methods
print("\n String Methods \n")
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.capitalize())
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

# Numbers
print("\n Numbers\n")
x = 1
x = 1.1
x = 1 + 2j  # complex

print(10/3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x+3
x += 3

# working with numbers

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

# Type Conversion

# x = input("x: ")
# y = x + 1
# print(type(x))
x = (input("x: "))
y = int(x) + 1
print(f"x: {x}, y: {y}")

# comparison operators

"""
10>3
10>=3
10<=20
10<20
10==10
10 == "10"
10 != "10"

"bag" > "apple"
"bag" == "BAG"
"""

# conditional statements

temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# ternary operator

age = 22
"""if age >= 18:
    # print("Eligible")
    message = "Eligible"
else:
    # print("Not eligible")
    message = "Not Eligible"""
# ternary here
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


# Logical operators
"""
and
or
not
"""

high_income = True
good_credit = True
student = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income or good_credit) and not student:
    print("eligible")
else:
    print("not eligible")

# short circuit evaluations
# if any of the arguments is false it short circuits and stop
if high_income and good_credit and not student:
    print("Eligible")

# Chaining Comparison Operators

if 18 <= age < 65:
    print("Eligible")

# quiz
# prints else statement so prints c.

# for loops
for number in range(3):  # range(1, 10, 2)
    print("Sending a message")
    print("Attempt", number+1, (number+1) * ".")

# for else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested Loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# iterables

print(type(5))
print(type(range(5)))  # range is iterable

for x in range(5):
    print(x)

for x in "Python":  # strings are iterable too
    print(x)

for x in [1, 2, 3, 4]:  # arrays are iterable too
    print(x)
"""
for item in shopping_cart:
    print(item)
"""

# While Loops
number = 100
while number > 0:
    print(number)
    number //= 2
"""
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)"""

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# exercise
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
print(f"We have {count} even numbers")

# Defining functions


def greet():
    print("Hi there")
    print("Welcome abroad")


greet()

# Arguments


def greetv2(f_name, l_name):
    print(f"Hi {f_name} {l_name}")
    print("Welcome abroad")


greetv2("ali", "veli")

# Types of functions
# 1- Perform a task , greet, print
# 2- Return a value ,round


def greett(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("hasan")

print(message)
print(get_greeting("salim"))
file = open("context.txt", "w")
file.write(message)
file.close()

print(greett("nonetry"))

# Keyword Arguments


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

print(increment(2, by=2))  # keyword argument here

# default arguments


def incrementt(number, by=1):
    return number + by


print(incrementt(2))
print(incrementt(2, 5))

# args xargs wait what


"""def multiply(x, y):
    return x * y


multiply(2, 3, 4, 5)
"""
"""
[2,3,4,5]

def multiply(*numbers):
    print(numbers)"""


def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number
        total *= number
    return total


print(multiply(2, 3, 4, 5, 6))
