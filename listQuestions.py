# Question 1: Create a list with 5 friends and ask user a friend name and
# add that name in the friend list,
# and print the list
# after that ask user to most important friend and add that friend at user choice

# Ex: [1,2,3,4,5]
# -> Enter anothe fiend: Raju
# [1,2,3,4,5,"Raju"]
# --> Most import afiedn: Billa
# --> Please location for billa: 1
# [1,"Billa",3,4,5,"Raju"]

friends = ["Prachi", "Gunjan", "Chaitnya", "Ahnis", "Harry"]

newFriend = input("Enter the name of another friend: ")
friends.append(newFriend)
print(friends)

mostImportantFriend = input("Enter the most important friend: ")
location = int(input("Please location for " + mostImportantFriend + ": "))
friends.insert(location, mostImportantFriend)
print(friends)


# Question 2:  Create a list of 10 number and print the list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)


# Qusetion 3: Create a list [1,10,100,3,6,8] and add 59 on 3 location after that append 5 and print list and length of list

numbers = [1, 10, 100, 3, 6, 8]
numbers.insert(3, 59)
numbers.append(5)
print("List of numbers is: ", numbers)
print("Length of the list is: ",len(numbers))


# Question 4: Find all of the words in a list of strings that are less than 4 letters

stringsList = ["ab", "abc", "abcd", "123", "1234", "12"]
result = []

for i in stringsList:
    if len(i) < 4:
        result.append(i)

print("All the words in the list of strings that are less than 4 letters are: ", result)


# Question 5: Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

result = []

numbers = range(20)

for i in numbers:
    if i % 2 == 0:
        result.append("even")
    else:
        result.append("odd")

print(result)


# Qusetion 6: Find all of the numbers from 1-1000 that are divisible by 7 

result = []

for i in range(1, 1001):
    if i % 7 == 0:
        result.append(i)

print("All the numbers divisible by 7 from 1 - 1000 are: ", result)


# Question 7: Count the number of spaces in a string

s = input("Enter a string: ")

spaceCount = 0

for i in s:
    if i == " ":
        spaceCount += 1

print("Number of spaces: ", spaceCount)

# Question 8: Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5

list_a = [1,2,3,4]
list_b = [2,3,4,5]

common = []

for i in list_a:
    if i in list_b:
        common.append(i)

print("The common numbers in the 2 lists are: ", common)