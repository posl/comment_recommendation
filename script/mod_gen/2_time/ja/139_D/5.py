def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print((n - 1) * (n // 2) + n % 2)
main()

if __name__ == '__main__':
    main()