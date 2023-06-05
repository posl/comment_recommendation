def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    elif n % 3 == 1:
        print(n // 3 * y + x)
    elif n % 3 == 2:
        print(n // 3 * y + 2 * x)

if __name__ == '__main__':
    main()