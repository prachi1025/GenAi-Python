# Enumerate function
# Enumerate function is used to add index to the list.

l = [11, 12, 13, 14, 15]

for i in range(0, len(l)):
    print(i, l[i])

print("--------")

# using enumerate
# keyword - enumerate
# syntax - enumerate(iterable)

for i in enumerate(l):
    print(i)  # returns tuple

for i,j in enumerate(l):
    print(i,j)

# enumerate function is basically used with dictionaries because they ahve key value pairs but index is not returned.

d = {"a": 1, "b": 2, "c": 3}

for i in enumerate(d.items()):
    print(i)

for i in enumerate(d.keys()):
    print(i)

for i in enumerate(d.values()):
    print(i)

# dictionary comprehension
# syntax- {key: value for (key, value) in iterable}

d = {i[1]: i[0] for i in d.items()}
print(d)