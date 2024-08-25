"""
Dictionaries are used to store data values in "key: value" pairs.
They are unordered, mutable (changable) & don't allow duplicate keys.
Dictionary works in pairs. The words act as "key" which means when we want to know the meaning of a work, we search for the word itself,
not the meaning. Here key is the search word and the meaning of the key is it's value.
If we need to store pair type key value in python, we store it in the form of Dictionary data values.
"""

info = {
    "name" : "Suddha",
    "Age" : 29,
    "Academic Scores" : [7.2, 6.3, 5.8],
    "Subjects" : ("English", "Science", "Maths", "History", "Geography")
}
print(info)

# We cannot make list and dict a key as they are immutable and hence their values cannot be changed. Keys cannot be duplicate.

print(type(info))
print(info["Academic Scores"])  # Use ["Key"] format to print the value of the searched key from the dictionary. Keys are case sensitive.
print(info["Subjects"])
info["name"] = "Suddhasil"  # Use ["Key"] format to search and = "Value" to update the value of the key searched.
info["Age"] = 30    # Also if other value for the same key is entered in the same format, python will overwrite the value and replace old with new value.
info["New Key"] = "New Value"   # Use same code format to change the value and add new key and it's value to the dictionary.
print(info)

null_dict = {}  # Created empty dictionary
null_dict["name"] = "Aabir" # Adding values to the empty dictionary
null_dict["age"] = 30
null_dict["Occupation"] = "Salaried Person"
null_dict["Hobbie"] = "Video Games"
null_dict["Birthmark"] = "Dots behind earlobe"

print(null_dict)

employee = {}

employee["Name"] = "Tuhin Manna"
employee["Tenurity in BT"] = 5.8
employee["LOB"] = "BT Business"
employee["Designation"] = "CDM Analyst"
employee["Application Scores"] = {      # This is called nested dictionary where the key in the dictionary is further converted to a dictionary itself, containing various sub keys and values.
    "1st App" : 5.2,
    "2nd App" : 6.3,
    "3rd App" : 9.8,
    "4th App" : 6.9,
    "5th App" : 4.5
}

print(employee)
print(employee["Application Scores"]["3rd App"])    # Use [] to dig deeper into sub-dictionaries and values.

"""
Dictionary Methods
myDict.keys()   #returns all keys
myDict.values() #returns all values
myDict.items()  #returns all (key, val) pairs as tuples
myDict.get("key") / myDict["key"]   #returns the key according to value
myDict.update(newDict)  #inserts the specified items to the dictionary
"""

print(employee.keys())
print(employee.values())
print(employee.items())
print(len(employee))
print(employee.get("Designation "))

# We can convert the data type from dict keys to list or tuples. To do that we do "type cast".

print(list(employee.items()))


"""
Set in Python
Collection of unordered items. Each element in a set must be unique and immutable. Remember, sets are mutable, but elements within sets are immutable.
Elements cannot be repeated. Only 1 occurrance is possible for each element.
We cannot store list and dict in set as they are mutable (can be changed). Other data types can be stored as they are immutable.
Dictionary and sets both use {}
"""

set1 = {1, 2, 3, 4, 5, 6}

print(set1)

print(type(set1))

set2 = {"My world", 2, 3.14,"My world", 2, 4, 3.14}     #The output of a set is in different sequence everytime it is run (random order). Hence, it is called unordered.
print(set2)
print(len(set2))    #Will show the length after removing all duplicate values. Only length of set with distinct values as output will reflect.

"""
Set Methods
set.add(el) #adds an element
set.remove(el)  #removes an existing element from set
set.clear() #empties the set
set.pop()   #removes a random value
set.union(set2) #combines both set values & returns a new set
set.intersection(set2)  #combines common values & returns a new set 
"""

empty_set = set()   #Syntax for creating empty set.

empty_set.add(3.14)
empty_set.add("Learning Python")
empty_set.add("Pie Thon")
empty_set.add(29)
empty_set.add(3.14)

print(empty_set)

# Dictionary for programming related terms

programming_dict = {
    "Algorithm": "A step-by-step procedure for solving a problem.",
    "Array": "A collection of elements, identified by index or key.",
    "Binary": "A system of numbers using only 0 and 1.",
    "Bug": "An error or flaw in software that causes unexpected behavior.",
    "Class": "A blueprint for creating objects in object-oriented programming.",
    "Compiler": "A program that translates source code into executable code.",
    "Data": "Information that can be processed or analyzed.",
    "Database": "A structured collection of data stored electronically.",
    "Debugging": "The process of identifying and fixing errors in software.",
    "Encapsulation": "The bundling of data with methods that operate on that data.",
    "Function": "A block of code that performs a specific task.",
    "IDE": "Integrated Development Environment, a software application for coding.",
    "Inheritance": "A mechanism in object-oriented programming that allows a class to inherit attributes and methods from another class.",
    "Instance": "An individual object of a specific class.",
    "Interpreter": "A program that executes code line by line.",
    "Loop": "A sequence of instructions that repeats until a certain condition is met.",
    "Method": "A function that is defined within a class and operates on instances of that class.",
    "Object": "An instance of a class containing data and methods.",
    "Polymorphism": "The ability of different classes to be treated as instances of the same class through a common interface.",
    "Recursion": "The process in which a function calls itself.",
    "Syntax": "The set of rules that defines the structure of a programming language.",
    "Variable": "A reserved memory location to store values.",
    "Tuple": "An immutable collection of ordered items.",
    "String": "A sequence of characters.",
    "Dictionary": "A collection of key-value pairs.",
    "Module": "A file containing Python definitions and statements that can be imported into a program.",
    "Package": "A collection of Python modules grouped together.",
    "Exception": "An event that disrupts the normal flow of a program.",
    "List": "An ordered collection of items that can be changed (mutable).",
    "Queue": "A collection of items in which the first item added is the first item removed (FIFO).",
    "Stack": "A collection of items in which the last item added is the first item removed (LIFO).",
    "Set": "An unordered collection of unique items.",
    "Lambda": "An anonymous function in Python, defined using the `lambda` keyword.",
    "Decorator": "A function that modifies the behavior of another function or method.",
    "Closure": "A function object that remembers values in enclosing scopes even if they are not present in memory.",
    "Generator": "A function that returns an iterator which we can iterate over one value at a time.",
    "Comprehension": "A concise way to create lists, sets, or dictionaries in Python.",
    "Operator": "A symbol that performs an operation on one or more operands.",
    "Operand": "A value on which an operator acts.",
    "Namespace": "A container that holds a set of identifiers (names) and their associated objects."
}
print(programming_dict)