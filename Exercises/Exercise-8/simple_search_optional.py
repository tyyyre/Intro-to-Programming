# Exercise 8: Simple Search (Optional)
# Allow user to input search term

users = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
lookingfor = input("Enter a name to search: ")

if lookingfor in users:
    print(f"User {lookingfor} found!")
else:
    print(f"User {lookingfor} not found!")