print("My name is Suddhasil Ghosh")

print(23 + 53)

name = "Suddha"
age = 29
price = 108

print("My name is:", name)
print("My age is:", age)
print("The price for my course is:", price)

age = 31
age2 = age

print(age2)

"""""
Multi line comments can be quoted with 3-4 double quotes at the beginning and end of the full comments.
Variables (Identifiers) can be a combination of alpha-numerica and upper & lower case.
Variable cannot start with digit. Eg. Variable1 is valid, 1Variable is not
Can't use special characters or symbols in variable
"""""

name = "Suddha"
age = 29
price = 108.00

print(type(name))
print(type(age))
print(type(price))

# Data types are:- Integers, String, Float, Boolean, None
# We can comment out multiple lines by pressing Ctrl+/

a = 10
b = 2

print(a - b)
print(a + b)
print(a * b)
print(a / b)
print(a % b) #modulo which divides and gives reminder as the answer
print(a ** b) # a to the power b

# Relational/Comparison operators (equal to ==, not equal !=, >, <, >=, <=)

d = 50
e = 20

print(d == e) # basic comparison operations give boolean values as output
print(d != e) # it gives "True" as outcome as the statement is correct (d is not equal to e), likewise
print(d >= e)
print(d <= e)

# Assignment Operators are used to assign values to variables, like = sign

num = 50
num = num + 10
num += 20
print(num) #will give result as 20, adding 10 value to the initial num value which was 10

# Logical operators (not, and, or) work on Boolean values

print(not False)
print(not True)

print(not(d == e))

val1 = True
val2 = False

print("and operator:", val1 and val2)

print("or operator:", val1 or val2)

print("or operator:", (d == e) or (d > e)) # d = 50, e = 20. OR operator prefers "True" Boolean value. Hence if even 1 condition is true, it will print True as the final output

"""
Type conversion and casting
a,b = 1,2.0 where, a is integer and b is floating value
Conversion - Python interpreter automatically converts the type of the variable.
Casting - Programmer instructs the type to which the variable is to be converted.
"""

a = 2
b = 4.25
sum = a + b # 2.0+4.25 = 6.25
print(sum)
#conversion function converts a value type to it's superior value type in the equation. Here, float is superior to integer as it contains more detailed information of the value

"""""
To cast type of a variable to which you want to convert, type:-
converted type(value)
"""""
a,b = 1,2.0
a = float("1")
print(type(a))

"""
Input statement is used to accept values (using keyboard) from user
input() result for input is always str
int(input())
float(input())
"""
name = input("Enter your name:")
age = input("Enter your age:")

print("welcome to the coding world",name, "of the age",age)

"""
In order to print a statement without value, program will need values from user, hence it will ask for user input. to make program ask user for the required input,
add variable with input function and "statement for seeking user input: ? - "
then, print("with the rest of the phrases",variable)
"""

place = input("Key in the place where you wanna be:")
time = input("Key in the year by when you wanna visit the place:")

print("My dream is to visit the place named",place, "by the year",time)

"""
The type of output will always be in string for input function. Hence, in order to change the type of the output to the appropriate one, you need to data cast.
To data cast,
var = type(input("string data type statement"))
print(type(var),var) = to see the data converted to required type
"""
name = input("enter your name: ")
age = int(input("enter your age: "))
year10 = int(input("enter year of passing Class X: "))
year12 = int(input("enter year of passing class XII exam: "))
profession = str(input("enter where you work: "))

print("My name is",name)
print("My age is",age)
print("I passed Class X in the year",year10)
print("I passed Class XII in the year",year12)
print("and I work in",profession)
