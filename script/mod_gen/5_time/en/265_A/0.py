def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    elif n % 3 == 1:
        print((n // 3 - 1) * y + x)
    else:
        print((n // 3) * y + x * 2)

if __name__ == '__main__':
    main()