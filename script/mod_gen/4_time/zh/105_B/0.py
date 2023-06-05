def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 4 == 1 or N % 7 == 1 or N % 11 == 1:
        print("Yes")
    elif N % 4 == 2 or N % 7 == 2 or N % 11 == 2:
        print("Yes")
    elif N % 4 == 3 or N % 7 == 3 or N % 11 == 3:
        print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()