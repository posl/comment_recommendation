def main():
    num = input()
    if num[0] == num[1] == num[2] == num[3]:
        print("Weak")
    elif num[0] == num[1] == num[2] or num[1] == num[2] == num[3]:
        print("Weak")
    elif num[0] == str(int(num[1]) - 1) == str(int(num[2]) - 2) == str(int(num[3]) - 3):
        print("Weak")
    elif num[0] == str(int(num[1]) - 1) == str(int(num[2]) - 2) == str(int(num[3]) + 7):
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()