correctpassword = 12345
allowedattempts = 5

while True:
    password = int(input("Enter your password: "))
    allowedattempts -= 1
    if allowedattempts == 0:
        print("No more attempts left. Access denied!")
        break
    if password == correctpassword:
        print("Access granted!")
        break
    else:
        print("Access denied! Try again. Attempts left:", allowedattempts)
