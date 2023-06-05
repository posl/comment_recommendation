def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 4 == 3:
        print("Yes")
    elif N % 7 == 6:
        print("Yes")
    elif N % 11 == 9:
        print("Yes")
    elif N % 4 == 2:
        print("Yes")
    elif N % 7 == 5:
        print("Yes")
    elif N % 11 == 7:
        print("Yes")
    elif N % 4 == 1:
        print("Yes")
    elif N % 7 == 4:
        print("Yes")
    elif N % 11 == 2:
        print("Yes")
    elif N % 4 == 0:
        print("Yes")
    elif N % 7 == 0:
        print("Yes")
    elif N % 11 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()