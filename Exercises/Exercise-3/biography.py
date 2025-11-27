# Exercise 3: Biography (Basic Requirements)
# This program asks the user for name, hometown, and age and prints them

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(bio["name"] + "\n" + bio["hometown"] + "\n" + bio["age"])