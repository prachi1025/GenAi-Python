# Modules - Modules are Python files that contain code that can be imported and used in other Python files.
# They are a way to organize and reuse code in Python.
# Modules are imported using the import keyword.

# Libraries - Libraries are modules that are pre-built and made available for use in Python.
# They are a way to add functionality to your code without having to write the code yourself.
# Libraries are imported using the import keyword.

# pip install <library_name>

import random

print(random.randint(1, 10)) # generates a random number between 1 and 10

l = ["yellow", "green", "blue", "red", "pink"]
print(random.choice(l)) # generates a random element from the list
print(random.choices(l, k=2)) # generates 2 random elements from the list


import time # time module is used to add delay to the program
print("Hello this is time")

time.sleep(5) # waits for 5 seconds

print("after 5 seconds")


import datetime # datetime module is used to get the current date and time
print(datetime.datetime.now()) # prints the current date and time
print(datetime.date.today()) # prints the current date


# infinite loop that will print the current date and time every second
while True: 
    print(datetime.datetime.now())
    time.sleep(1)