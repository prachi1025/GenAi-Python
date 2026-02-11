# Question 1: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return ‘not a valid string’ instead of the empty string
# Sample string: - “Coder roots”
# Expected result - “cots”
# Sample string - “New year”
# Expected result - “near”

s = input("Enter a string: ")

if len(s) < 2:
    print("Not a valid string")
else:
    print(s[:2] + s[-2:])


# Question 2: Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string
# Sample String : 'coder', 'roots'
# Expected Result : 'roder coots'

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(s2[0] + s1[1:] + " " + s1[0] + s2[1:])


# Question 3: Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

s = input("Enter a string: ")

if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")


# Question 4: Write a Python program to remove the nth index character from a nonempty string

s = input("Enter a string: ")
n = int(input("Enter an index: "))

print(s[:n] + s[n + 1:])