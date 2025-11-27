# Exercise 3: Biography (Advanced Requirements)
# This version handles:
# - Multiple word inputs (e.g. first + last name)
# - Input for name, hometown, and age
# - Basic validation to prevent non-numeric age values

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

# Store the information in a dictionary
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values on separate lines
print(bio["name"] + "\n" + bio["hometown"] + "\n" + bio["age"])
