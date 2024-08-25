# List - is a built in data type that stores set of values. It can store elements of different types (integer, float, string, etc.)
# Apply [] brackets to store multiple list of values.

marks = [94,52,64,48,63,57]
print(marks)
print(type(marks))

# List is identified as a separate class.

print(marks[2])
print(marks[4])
print(len(marks))


# Strings and Tuples are "IMMUTABLE" (not editable) and lists are "MUTABLE" in python. Which means MUTABLE can be changed but IMMUTABLE can't.
# In index - positioning values in string, we could access but NOT change values, but we can both access and change values in list.
"""
List Slicing - similar to string slicing.
list_name[starting_idx : ending_idx] ending index not included
"""

print(marks[1 : 5])

# List Methods - Methods are specific to type of input/subjects.

# list.append(value). Append method returns 'none'.

var = [5, 7, 9]
var.append(6)      # var.append(value), then print the "var" to update the list. It is called mutating the list.

print(var)

#   list.sort() -   sorting in ascending order
var.sort()
print(var)

#   list.sort(reverse = True) -   sorting in descending order
var.sort(reverse = True)
print(var)

#   list.reverse() -   reverses list sequence
var.reverse()
print(var)

# Note = The value of variable "var" will keep on updating with every function executed. The next print function will reflect the last function run on updated value.
#   list.insert(idx, el) -   insert element at index (position)

var.insert(3, 24)
print(var)

list = [3, 6, 0, 8, 2, 5, 1, 4, 9, 7]

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(3, 10)
print(list)

# list.remove(value) removes 1st occurrance of the value.

list.remove(10)
print(list)

# list.pop(idx) removes element at index.

list.insert(3, 10)
print(list)

list.pop(3)

print(list)

# Tuples - Built in data type which lets us create immutable sequence of values, like strings. Cannot edit components. Can only access them.

tup = (1, 3, 4, 6, 5, 7, 2, 4)

print(tup)
print(tup[2])
print(tup[5])
tup[2] = 8      # Will reflect error message showing "Tuple" object does not support item assignment

tup1 = () #Empty tuple
print(tup1)
print(type(tup1))

# Single Value Tuple is to be created with a ", " - right way. If written without ", " python will consider it as integer for numerical value.

tup2 = (4, )
print(tup2)
print(type(tup2))

"""
Tuple methods
tuple.index(value) returns index of first occurrence
tuple.count(value) counts total occurrences
"""

tup.index(2)    # Output 4
tup.count(4)    # Output 2

# List are written under [] whereas tuples are written with ().