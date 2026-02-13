# Question 1: Word Frequency with Sorting Write a Python program that takes a sentence as input and stores word frequencies in a dictionary. Finally, print the dictionary sorted by frequency in descending order.

# Input:
# "python is easy and python is very easy"

# Output:
# {'python': 2, 'easy': 2, 'is': 1, 'and': 1, 'very': 1}

inputSentence = input("Enter a sentence: ")

words = inputSentence.split()

wordFrequency = {}

for word in words:
    if word in wordFrequency:
        wordFrequency[word] += 1
    else:
        wordFrequency[word] = 1

items = wordFrequency.items()

sortedItems = sorted(items, key=lambda x: x[1], reverse=True)

wordFrequency = dict(sortedItems)

print("The Sorted word frequency dictionary is:", wordFrequency)


# Question 2: Student Grade Report
# Create a dictionary with student names as keys and their marks as values.

studentReport = {
    "Prachi": 100,
    "Gunjan": 100,
    "Chaitnya": 100,
    "Ahnis": 100,
    "Harry": 50
}

# Write a program that:
#  Calculates the average marks

averageMarks = sum(studentReport.values()) / len(studentReport)
print("Average Marks:", averageMarks)

#  Prints names of students scoring above average

print("Names of students scoring above average:")
for name, marks in studentReport.items():
    if marks > averageMarks:
        print(name)


# 3. Combine Dictionaries with Conditions
# Given two dictionaries, merge them such that:
# If a key exists in both dictionaries, keep the maximum value
# Otherwise, keep the original key–value pair
# Example:
# {'a': 50, 'b': 30, 'c': 70}
# {'b': 60, 'c': 65, 'd': 40}
# Output:
# {'a': 50, 'b': 60, 'c': 70, 'd': 40}

d1 = {'a': 50, 'b': 30, 'c': 70}
d2 = {'b': 60, 'c': 65, 'd': 40}

mergedDict = {}

for key in d1:
    if key in d2:
        mergedDict[key] = max(d1[key], d2[key])
    else:
        mergedDict[key] = d1[key]

for key in d2:
    if key not in mergedDict:
        mergedDict[key] = d2[key]

print("Merged Dictionary:", mergedDict)


# 4. Find Key with Maximum Length Value
# Given a dictionary where values are strings, write a program to find the key whose value has the
# maximum length.
# Example:
# {'name': 'Alice', 'city': 'Bangalore', 'course': 'Data Science'}
# Output:
# course

d = {'name': 'Alice', 'city': 'Bangalore', 'course': 'Data Science'}

maxKey = None
maxLength = 0

for key, value in d.items():
    if len(value) > maxLength:
        maxLength = len(value)
        maxKey = key

print("Key with maximum length value:", maxKey)


# 5. Filter Dictionary by Value Range
# Write a Python program to filter a dictionary and create a new dictionary containing only those
# key–value pairs where the value lies between 10 and 50 (inclusive).

d = {'a': 1, 'b': 2, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

filteredDict = {key: value for key, value in d.items() if 10 <= value <= 50}

print("Filtered Dictionary:", filteredDict)


# 6. Dictionary-Based Voting System
# Create a dictionary to store votes for candidates.
# Write a program that:
#  Accepts votes as input
#  Counts votes using a dictionary
#  Displays the winner (candidate with maximum votes)

votes = {}

n = int(input("Enter the number of votes: "))

for i in range(n):
    candidate = input("Enter the name of the candidate: ")
    
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

winner = ""
maxVotes = 0

for candidate in votes:
    if votes[candidate] > maxVotes:
        maxVotes = votes[candidate]
        winner = candidate

print("The winner is:", winner)
print("Number of votes:", maxVotes)


# 7. Replace Values Using Another Dictionary
# Given two dictionaries:

#  The first dictionary contains keys and values
#  The second dictionary contains replacement values

# Write a program to replace values of the first dictionary only if the key exists in the second dictionary.

# Example:
# data = {'a': 10, 'b': 20, 'c': 30}
# update = {'b': 200, 'c': 300}
# Output:
# {'a': 10, 'b': 200, 'c': 300}

data = {'a': 10, 'b': 20, 'c': 30}
update = {'b': 200, 'c': 300}

for key in update:
    if key in data:
        data[key] = update[key]

print(data)
