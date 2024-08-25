# Store following word meanings in a python dictionary. Table - a piece of furniture, list of facts & figures; cat - a small animal

word = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture" , "list of facts & figures"]  #Use [] to add list of values for a key in dictionary
}
print(word)

# You are given list of subjects for students. Assume one classsroom is required for 1 subject. How many classrooms are needed by all students?
# "Python", "Java", "C++", "Javascript", "Java", "C++", "C", "Python", "C"

subjects = {"Python", "Java", "C++", "Javascript", "Java", "C++", "C", "Python", "C"}

print(subjects)
print(len(subjects),"classrooms are needed by all students.")

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with empty dict and add 1 by 1. Subject name as key and marks as values.

marks = {}
"""
marks["Subjects"] = {
    input("Subject 1: ") : 85,
    input("Subject 2: ") : 76,
    input("Subject 3: ") : 64
}
"""
x = int(input("Physics : "))
marks.update({"Physics" : x})

y = int(input("Chemistry : "))
marks.update({"Chemistry" : y})

z = int(input("Maths : "))
marks.update({"Maths" : z})

print(marks)

# Figure out a way to store 9 & 9.0 as separate values in the set. You can take help of built in data-types

num = {9, "9.0"}
print(num)  # As python would consider the "hash" values of the elements to be smae, hence to avoid that one element's data type is changed to string.