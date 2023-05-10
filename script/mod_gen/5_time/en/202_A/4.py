def diceRoll():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if (a >= 1 and a <= 6) and (b >= 1 and b <= 6) and (c >= 1 and c <= 6):
        print(7-a+7-b+7-c)
    else:
        print("Invalid number")
diceRoll()

if __name__ == '__main__':
    diceRoll()