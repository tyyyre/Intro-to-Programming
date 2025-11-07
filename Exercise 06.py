correctpassword = 12345

while True:
    password = int(input("Enter your password: "))
    if password == correctpassword:
        print("Access granted!")
        break
    else:
        print("Access denied! Try again.")
