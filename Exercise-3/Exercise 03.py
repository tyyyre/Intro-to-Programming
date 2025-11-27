# Exercise 3: Biography (Basic Requirements)
# This program asks the user for their name, hometown, and age,
# stores the information in a dictionary, and prints it on separate lines.

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

# Store values in a dictionary as required
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print the values on separate lines using one print() statement
print(bio["name"] + "\n" + bio["hometown"] + "\n" + bio["age"])
