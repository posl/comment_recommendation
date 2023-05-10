def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print((y // 3) * n)
    elif n % 3 == 1:
        print((y // 3) * n + x)
    else:
        print((y // 3) * n + (y // 3) + x)

if __name__ == '__main__':
    main()