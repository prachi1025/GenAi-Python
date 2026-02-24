# Exception Handling

# Errors - Syntax Errors, definition - Errors that occur when the code violates the syntax rules of the programming language. These errors prevent the code from being executed and must be fixed before the program can run.

# Exceptions - Runtime Errors, definition - Errors that occur during the execution of the code. These errors can be handled by the program to prevent the program from crashing. 
# Logical Errors - Errors that occur when the code is not logical. These errors prevent the code from being executed and must be fixed before the program can run.

# try, except, else, finally

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try: # Code that may raise an exception
    result = a / b
    print("Result:", result)
except Exception as e: # Code to handle the exception
    print("Error:", e)
else: # Code to execute if no exception occurs
    print("No error")
finally: # Code to execute regardless of whether an exception occurs
    print("Program completed")

print("Very Important Line")


# Multiple Exceptions - We can use multiple except blocks to handle different types of exceptions
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

l = [1, 2, 3]

try: 
    print(a/b)
    print(l[4])
except ZeroDivisionError as e: # code to handle zero division error
    print("Error:", e)
except IndexError as e: # code to handle index error
    print("Error:", e)
else:
    print("No error")
finally:
    print("Program completed")

# in the above program if we try to divide a number by zero then it will raise a ZeroDivisionError exception and if we try to access an index that does not exist in the list then it will raise an IndexError exception, but whatever exception is caught first, its except block is executed and the other except blocks are not executed