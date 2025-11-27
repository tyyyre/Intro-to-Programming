# Exercise 6: Brute Force Attack (Basic Requirements)
# This program keeps asking for the password until the correct one is entered.

correctpassword = 12345

password = None
while password != correctpassword:
    password = int(input("Enter your password: "))

print("Access granted!")
