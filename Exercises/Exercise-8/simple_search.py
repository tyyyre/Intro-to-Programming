# Exercise 8: Simple Search
# Search a predefined list for "Sam"

users = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
lookingfor = "Sam"

if lookingfor in users:
    print(f"User {lookingfor} found!")
else:
    print(f"User {lookingfor} not found!")