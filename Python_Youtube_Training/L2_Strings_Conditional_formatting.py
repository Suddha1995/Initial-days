str1 = "This is a string.\nWe are creating it in python." # \n is for next line, which prints the characters after it in next line
print(str1)

str2 = "This is a string.\tWe are creating it in python." # \t is for tab, which gives extra spaces between characters.
print(str2)

# We can join two strings through concatination "(+) operator"

str3 = "I will have to "
str4 = "work sincerely to excel at my new role."
sentence = (str3 + str4)

sentence = print(sentence)

length1 = len(str1)
length2 = len(str2)
length3 = len(str3)
length4 = len(str4)

print(length1)
print(length2)
print(length3)
print(length4)

# Assign length as variable of the string you want to find the length for. Then print the variable.

"""
Indexing = Denotes the position of each characters in a string.
It starts with 0 - 9. (The first character gets the index named 0.)
It helps in accessing the desired character at any index from the string.
To access a particular character from the string, variable[2], you will get the character which is in 3rd position of the string, as index starts with 0.
We can only access characters through index. We cannot manipulate or edit, replace characters with other character in python.
"""

str5 = "My home sweet home."
ch = str5[3]
print(ch)

"""
Slicing = Accessing parts of a string. Very important for machine learning.
While applying machine learning algorithms we need to extract relevant information from the data.
Variable[starting_index : ending_index]     ending_index is not included.
"""

var = "I will have to work sincerely to excel at my new role."
print(var[2 : 11])
print(var[ : 15])
print(var[4 : ])

"""
Negative Index = Feature only found in python. It starts with -1 and moves from right to left. Counted backward.
"""

str6 = "Apple"

print(str6[-3 : ])
print(str6[ : -2])

"""
String Functions
str.endswith("string") = returns True/False if string ends with the characters mentioned in the function matches/not matches.
str.capitalize() = capitalizes 1st character
str.replace(old, new) = replaces all occurrences of old
str.find(word) = returns 1st index of 1st occurance
str.count("am") = counts the occurrance of substring
"""

var2 = "i am studying python from apna college."
print(var2.capitalize())

print(var2.replace("apna college","youtube training videos"))

print(var2.find("apna")) # prints the 1st occurrance or 1st index of the word search for.

# If we are searching for a word or character which is not there in the string, it will print -1 as it's not a valid position or index.

print(var2.count("from"))

"""
Conditional Statements
if-elif-else(SYNTAX)
if(condition):
    Statement1
elif(condition):
    Statement2
else(condition):
    StatementN
"""

age = 27
if(age >= 18):
    print("Eligible to apply for voter card")

Signal = "Green"

if(Signal == "Red"):
    print("Stop the car")       # Indentation (Proper spacing) is the space we give to continue the code and identify it as part of the continued code in previous line.
elif(Signal == "Yellow"):
    print("Look Around")
if(Signal == "Green"):
    print("Go")

# Note - "=" single equal is used to assign values to a variable (assign operator). "==" double equal is used to compare value to see if they are same (equal comparison operator)

"""
"If" condition will be always checked by Python while running the code. "elif" will only be checked if the "if" condition is not fulfilled. "else" statement is written at last. No condition
is chedcked at all as if other conditions fail, then the value assigned to else function will reflect. It is only used once.
"""

marks = int(input("Enter your marks: "))

if(marks > 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print("Grade of the student -> ", Grade)


assigned_number = 15

if((input("Enter your number = ") > assigned_number)):
    print("Entered number greater than assigned number.")
elif((input("Enter your number = ") == assigned_number)):
    print("Entered number equal to assigned number.")
else:
    print("Entered number lesser than assigned number.")