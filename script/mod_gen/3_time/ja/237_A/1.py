def main():
    n = int(input())
    if -2147483648 <= n < 2147483648:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()