def main():
    S = input()
    if S == "Monday":
        print("5")
    elif S == "Tuesday":
        print("4")
    elif S == "Wednesday":
        print("3")
    elif S == "Thursday":
        print("2")
    elif S == "Friday":
        print("1")
    elif S == "Saturday":
        print("0")
    elif S == "Sunday":
        print("0")
    else:
        print("Invalid Input")

if __name__ == '__main__':
    main()