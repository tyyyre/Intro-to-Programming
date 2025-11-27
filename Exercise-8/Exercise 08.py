# Exercise 8: Simple Search
# This program searches for a user-input name within a predefined list of names.

lookingfor = input("What user are you looking for? ")

users = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

if lookingfor in users:
    print(f"User {lookingfor} found!")
else:
    print(f"User {lookingfor} not found!")
