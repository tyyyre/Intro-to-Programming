# Exercise 10: Is It Even?
# This program checks if a user-entered number is even or odd.

def ask_number():
    return int(input("Enter a number: "))

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    num = ask_number()
    result = check_even_odd(num)
    print(f"The number {num} is {result}.")

if __name__ == "__main__":
    main()
