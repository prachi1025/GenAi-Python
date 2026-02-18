# Q1 - Given a list of numbers, print the sum of numbers present at even index positions.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in range(0, len(numbers), 2):
    sum += numbers[i]
print("The sum of all the elemnets at even indices is: ", sum)


print("========================================================")


# Q2 - Write a program to count how many times each character appears in a given string.

s = input("Enter a string: ")
charFrequency = {}

for ch in s: 
    if ch in charFrequency:
        charFrequency[ch] += 1
    else:
        charFrequency[ch] = 1

print("The word frequency dictionary is: ", charFrequency)


print("========================================================")


# Q3 - Write a function that takes a string and returns:
# • number of uppercase letters
# • number of lowercase letters

def countUpperLower(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    return upper, lower

s = input("Enter a string: ")
upper, lower = countUpperLower(s)
print("Number of uppercase letters: ", upper)
print("Number of lowercase letters: ", lower)


print("========================================================")


# Q4 - Given two lists:

subjects = ["Math", "Physics", "Chemistry"]
marks = [85, 78, 92]

# Use zip() to create a dictionary and print the subject with the highest marks.

dictionary = dict(zip(subjects, marks))
print("The subject with the highest marks is: ", max(dictionary, key=dictionary.get))


print("========================================================")


# Q5 - Using enumerate(), print the index of all negative numbers in a list.

numbers = [10, -5, 3, -6, 23, -2]

print("The index of all negative numbers in the list are: ")

for i, num in enumerate(numbers):
    if num < 0:
        print(i)


print("========================================================")


# Q6 - Write a program to check whether two lists contain the same elements (order does not matter).

list1 = [1, 2, 3, 4, 5]
list2 = [5, 3, 4, 1, 2]

if sorted(list1) == sorted(list2):
    print("The lists contain the same elements.")
else:
    print("The lists do not contain the same elements.")


print("========================================================")


# Q7 - Write a program to print the pattern:
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


print("========================================================")


# Q8 - Write a program that removes duplicate elements from a list and keeps only unique elements.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = list(set(l))
print("The list without duplicates is: ", l)


print("========================================================")


# Q9 - Given:

names = ["A", "B", "C", "D"]
scores = [45, 78, 90, 60]

# Using zip() and enumerate(), print:
# 1 - A scored 45
# 2 - B scored 78

for i, (name, score) in enumerate(zip(names, scores)):
    print(i + 1, "-", name, "scored", score)


print("========================================================") 


# Q10 - Write a function that checks whether a list is increasing order or not.
# Return True if increasing, otherwise False.

def isIncreasingOrder(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

l = [1, 2, 3, 4, 5]
print("Is the list in increasing order? : ", isIncreasingOrder(l))


print("========================================================")


# Q11 - Write a program that:
# • Takes a sentence from the user
# • Prints the number of characters (excluding spaces)
# • Prints the sentence in uppercase
# • Prints the sentence reversed

sentence = input("Enter a sentence: ")

charCount = 0
for ch in sentence: 
    if ch != " ":
        charCount += 1

print("The number of characters (excluding spaces) is: ", charCount)

print("The sentence in uppercase is: ", sentence.upper())

print("The sentence reversed is: ", sentence[::-1])


print("========================================================")


# Q12 - Write a program that keeps asking the user to enter a number.
# Stop the loop when the user enters 0, then print the total sum of all entered numbers.

total = 0

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total += num

print("The total sum of all entered numbers is: ", total)