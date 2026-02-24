#1
#Input student details

name=input("enter name:")
studentClass=input("enter class:")
section=input("enter section:")
 
mathsMarks=int(input("enter maths marks:"))
physicsMarks=int(input("enter physics marks:"))
chemistryMarks=int(input("enter chemistry marks:"))
englishMarks=int(input("enter english marks:"))
biologyMarks=int(input("enter biology marks:"))
 
totalMarks=mathsMarks+physicsMarks+chemistryMarks+englishMarks+biologyMarks
percentage=totalMarks/5

print("---student details---")
print("name:",name)
print("class:",studentClass)
print("section:",section)
print("total marks:",totalMarks)
print("percentage:",percentage,"%")


#2
#input 3 numbers and return sum of them

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
n3=int(input("enter third number:"))

sum=n1+n2+n3
print("sum:",sum)


#3
#input a number and return a square of it

n=int(input("enter number:"))
square=n*n
print("square:",square)


#4
#Celsius string to Fahrenheit Conversion

# Take temperature as string
celsius_str = input("Enter temperature in Celsius: ")

# Convert string to float
celsius = float(celsius_str)

# Convert to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Print result
print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)


#5 
# Write a program to calculate the remainder when a number is divided by another number.
# Input: Two integers from the user.
# Output: Quotient and remainder.

num1 = int(input("enter num1:"))
num2 = int(input("enter num2:" ))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient:", quotient)
print("Remainder:", remainder)


#6
# simple interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("The simple interest is:", simple_interest)