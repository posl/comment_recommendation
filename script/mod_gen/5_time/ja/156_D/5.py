def main():
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if b - a == 1:
        print((n - a) * (n - b) % (10**9 + 7))
    else:
        print((n - a) * (n - b) * (n - b - 1) % (10**9 + 7))

if __name__ == '__main__':
    main()