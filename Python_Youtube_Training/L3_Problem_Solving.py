# WAP asking user to enter names of 3 favourite movies & store them in a list

movies = []
movies.append(input("Enter 1st movie: "))
movies.append(input("Enter 2nd movie: "))
movies.append(input("Enter 3rd movie: "))

print(movies)   # Appending data to a list after every line, adding elements and length to the list.

# WAP to check if the list contains palindrome of elements. It reads same from both ends.

seq = [1,2,3,4,3,2,1]

seq.reverse()

print(seq)

# WAP to check if the list contains palindrome of elements. Use code to check if they are pelindrome.

con = [1,3,5,7,5,3,1]
che = [1,3,5,7,9,5,6]

copycon1 = con.copy()
copycon1.reverse()

if(con == copycon1):
    print("PELINDROME")
else:
    print("Not a PELINDROME")

copyche1 = che.copy()
copyche1.reverse()

if(che == copyche1):
    print("PELINDROME")
else:
    print("Not a PELINDROME")

# WAP to count number of students with grade "A" in the following tuple.

grade = ["C", "A", "D", "A", "B", "A", "D", "B", "D", "A"]

print(grade.count("A"))

# Store the above values in a list and sort them alphabetically. (1st apply sort function to the tuple separately, then print the updated variable)

grade.sort()

print(grade)