def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%11 == 0:
        print("Yes")
    elif n%4 == 3 or n%7 == 3 or n%11 == 3:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()