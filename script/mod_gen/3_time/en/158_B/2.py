def main():
    n, a, b = map(int, input().split())
    if n % (a + b) <= a:
        print((n // (a + b)) * a + n % (a + b))
    else:
        print((n // (a + b)) * a + a)

if __name__ == '__main__':
    main()