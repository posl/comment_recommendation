def main():
    n = int(input())
    if n % 7 == 0 or n % 4 == 0 or n % 11 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()