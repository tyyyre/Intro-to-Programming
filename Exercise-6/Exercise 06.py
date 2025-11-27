# Exercise 6: Brute Force Attack (Optional Requirements)
# This version allows only 5 attempts.

correctpassword = 12345
allowedattempts = 5

while allowedattempts > 0:
    password = int(input("Enter your password: "))
    allowedattempts -= 1

    if password == correctpassword:
        print("Access granted!")
        break
    else:
        print("Access denied! Try again.")
        print("Attempts left:", allowedattempts)

    if allowedattempts == 0:
        print("No more attempts left. Access denied!")
        print("Authorities have been alerted.")
