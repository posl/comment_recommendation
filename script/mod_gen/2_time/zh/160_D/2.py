def main():
    # n, x, y = map(int, input().split())
    # print(n, x, y)
    # print(type(n), type(x), type(y))
    # print(n + x + y)
    n = 10
    x = 4
    y = 8
    for k in range(1, n):
        if k < x:
            print(n - k)
        elif k < y:
            print(n - x + k - x)
        else:
            print(n - x + y - x - (k - y))
    return 0

if __name__ == '__main__':
    main()