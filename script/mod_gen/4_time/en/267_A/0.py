def main():
    s = input()
    if s == "Monday":
        print(5)
    elif s == "Tuesday":
        print(4)
    elif s == "Wednesday":
        print(3)
    elif s == "Thursday":
        print(2)
    elif s == "Friday":
        print(1)
    elif s == "Saturday":
        print(0)
    elif s == "Sunday":
        print(6)
    else:
        print("Invalid input")
main()

if __name__ == '__main__':
    main()