def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(x * n // 3)
    elif n % 3 == 1:
        print(min(x * (n - 1) // 3 + y, y * (n + 2) // 3))
    else:
        print(min(x * (n + 2) // 3, y * (n - 1) // 3 + x))

if __name__ == '__main__':
    main()