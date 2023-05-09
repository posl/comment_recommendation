def main():
    n, a, b = map(int, input().split())
    print((n // a) * (a + a * (n // a - 1)) // 2 + (n // b) * (b + b * (n // b - 1)) // 2 - (n // (a * b)) * (a * b + a * b * (n // (a * b) - 1)) // 2)

if __name__ == '__main__':
    main()