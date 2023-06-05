def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0 or N % 15 == 0 or N % 19 == 0 or N % 20 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()