def main():
    n = int(input())
    if n % 2 == 0:
        print(int(n / 2))
    else:
        print(int((n + 1) / 2))

if __name__ == '__main__':
    main()