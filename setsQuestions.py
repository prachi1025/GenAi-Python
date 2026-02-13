# Question 1: The Guest List
# You have two sets of names representing guests for Friday and Saturday.

friday = {"Alice", "Bob", "Charlie"}
saturday = {"Charlie", "David", "Eve"}

# • Task: Create a new set called all_guests that contains everyone attending at least one night.

all_guests = friday.union(saturday)
print("All guests: ", all_guests)

# • Task: Identify the guest who is attending both nights.

both_nights = friday.intersection(saturday)
print("Guests attending both nights: ", both_nights)


# Question 2: List Cleaner
# You have a list with duplicates: 

data = [1, 2, 2, 3, 4, 4, 4, 5]

# • Task: Convert this list into a set to remove duplicates, then add the number 6 to that set.

data = set(data)
data.add(6)
print("Updated data: ", data)


# Question 3: The Library Audit
# You have a set of all books owned by a library and a set of books currently checked out.

library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}

# • Task: Use a set operation to find the books currently sitting on the shelf (available).

available_books = library_books.difference(checked_out)
print("Currently available books: ", available_books)

# • Task: A student brings a "Don Quixote" to donate. Check if this book is not already in the library_books before adding it. 

if "Don Quixote" not in library_books:
    library_books.add("Don Quixote")
    print("Updated library books: ",library_books)


# Question 4: Permission Checker
# A user has 

user_permissions = {"read", "write"}

# The admin requirements for a folder are

admin_reqs = {"read", "write", "execute"}

# • Task: Use a method to check if the user has all the permissions required for admin access (Is the user's set a subset of the requirements?).

print("Does the user have admin access? ", admin_reqs.issubset(user_permissions))

# • Task: Find the specific permissions the user is missing.

print("Missing permissions: ", admin_reqs.difference(user_permissions))


# Question 5: The Log Analyzer
# You are given a dictionary where the keys are "Error Codes" and the values are lists of "Server IDs"
# where those errors occurred.
# Python

logs = {
"404": [10, 12, 15, 20],
"500": [12, 20, 22, 25],
"403": [10, 20, 30]
}

# • Task: Use a Set Comprehension to create a new set containing only the Server IDs that
# experienced every type of error (404, 500, AND 403).

commonErrorServers = {server for server in logs["404"] if server in logs["500"] and server in logs["403"]}
print("Servers with all errors: ", commonErrorServers)

# • Task: Identify the "Critical Servers"—these are servers that experienced a "500" error but
# never experienced a "404" error.

criticalServers = {server for server in logs["500"] if server not in logs["404"]}
print("Critical servers: ", criticalServers)