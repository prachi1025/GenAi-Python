# lambda functions are anonymous functions
# they are defined using lambda keyword

# syntax- lambda arguments: expression

# example
add = lambda x, y: x + y
print(add(3, 4))


# if else rule in lambda- we have to use if else together with lambda, if only cannot be used.
oddEven = lambda x: "Odd" if x % 2 != 0 else "Even" 
i=int(input("Enter a number: "))
print(oddEven(i))


# Map

# map(func,iterable)
# func- function
# iterable- list, tuple, set, dictionary

# example
l = [1, 2, 3, 4, 5]

def square(i):
    return i * i

s = map(square, l)
print(list(s))

# s = map(lambda x: x * x, l)
# print(list(s))

a = map(lambda i, j: i + j, [1, 2, 3], [4, 5, 6])
print(list(a))