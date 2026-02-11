#Question 1
# WAP Ask user to input a number and then month name corresponding to that number

monthNum = int(input("Enter a month number: "))

if monthNum == 1:
    print("January")
elif monthNum == 2:
    print("February")
elif monthNum == 3:
    print("March")
elif monthNum == 4:
    print("April")
elif monthNum == 5:
    print("May")
elif monthNum == 6:
    print("June")
elif monthNum == 7:
    print("July")
elif monthNum == 8:
    print("August")
elif monthNum == 9:
    print("September")
elif monthNum == 10:
    print("October")
elif monthNum == 11:
    print("November")
elif monthNum == 12:
    print("December")
else:
    print("Invalid month number")


#Question 2
#WAP Ask user to input 2 number,
#tell the followings
#1. Both number are equal or not
#2. Which is Bigger in both
#3. Either First Number is smaller or equal to Second Number
#4. Print your first name 5 times if first number is greater than second and print your surname 3 times if 1st no is less than second

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# 1. Check equal or not
if a == b:
    print("Both numbers are equal \n")
else:
    print("Numbers are not equal \n")

# 2. Bigger number
if a > b:
    print(a, " is bigger \n")
elif b > a:
    print(b, " is bigger \n")
else:
    print("Both are same \n")

# 3. First number smaller or equal to second
if a <= b:
    print(a, " is smaller or equal to ", b, "\n")
else:
    print(b, " is greater than ", b, "\n")

# 4. Print name based on condition
if a > b:
    for i in range(5):
        print("Prachi")
elif a < b:
    for i in range(3):
        print("Pargal")


#Question 3:
    # Using User input ask user to input 2 string and tell followings
    # 1. using == tell both string equal or not
    # 2. using is operator tell both equal or not

a = input("Enter first string: ")
b = input("Enter second string: ")
print("Using == operator: ", a == b)
print("Using is operator: ", a is b)


#Question 4:
    # ask user to input 2 string and convert it into numbers and using is op
    # tell both are equal or not

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

n1 = int(s1)
n2 = int(s2)

print("Using is operator: ", n1 is n2)


#Question 5:
    # Python program to calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1) :
    sum += i

print("Sum of all numbers from 1 to", n, "is:", sum)


#question 6 
# Ask user to input a number and tell all even number
#    upto that number
#  Eg:
#    input a num:29
#    Even are:
#    2,4,6,... 28

n = int(input("enter a number: "))

for i in range (2, n+1, 2) :
    print(i)


#question 7
    #6.  Ask user to input a number and tell all even number
#    upto that number
#  Eg:
#    input a num:29
#    Even are:
#    2,4,6,... 28

n = int(input("enter a number: "))
op = input("enter operator(+, -): ")

if op == "+" :
    for i in range (0, n,) :
        print(i)
else:
    for i in range (n, 0, -1) :
        print(i)