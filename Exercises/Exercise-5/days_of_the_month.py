# Exercise 5: Days of the Month (Basic)
# Prints the number of days for a given month

table = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

question = "Which month's number of days do you want to know?"
answer = int(input(question + " "))

if answer in table:
    print(f"Month {answer} has {table[answer]} days.")
else:
    print("Invalid month number!")