def main():
    n = int(input())
    if n // 100 == 7 or n % 100 // 10 == 7 or n % 10 == 7:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()