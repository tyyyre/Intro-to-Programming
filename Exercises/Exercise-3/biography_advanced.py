# Exercise 3: Biography (Advanced Requirements)
# This version demonstrates user input for multiple-word names and age as string

name = input("Enter your name (first and last): ")
hometown = input("Enter your hometown: ")
age = input("Enter your age: ")

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(bio["name"] + "\n" + bio["hometown"] + "\n" + bio["age"])