def AskNumber():
    number = int(input("Enter a number: "))
    return number

def CheckOddEven(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def main():
    num = AskNumber()
    result = CheckOddEven(num)
    print(f"The number {num} is {result}.")

if __name__ == "__main__":
    main()
