# Exercise 6: Brute Force Attack (Basic)
# Keep asking for password until correct

correctpassword = 12345
password = None

while password != correctpassword:
    password = int(input("Enter your password: "))

print("Access granted!")