def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int((n // 3) * y))
    elif n % 3 == 1:
        print(int((n // 3) * y + x))
    else:
        print(int((n // 3) * y + 2 * x))

if __name__ == '__main__':
    main()