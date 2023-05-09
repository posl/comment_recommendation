def main():
    n, a, b = map(int, input().split())
    if a + b > n:
        print(0)
    else:
        ans = pow(2, n, 10 ** 9 + 7) - 1
        c1 = 1
        c2 = 1
        for i in range(a):
            c1 = c1 * (n - i) % (10 ** 9 + 7)
            c2 = c2 * (a - i) % (10 ** 9 + 7)
        ans -= c1 * pow(c2, 10 ** 9 + 5, 10 ** 9 + 7)
        c1 = 1
        c2 = 1
        for i in range(b):
            c1 = c1 * (n - i) % (10 ** 9 + 7)
            c2 = c2 * (b - i) % (10 ** 9 + 7)
        ans -= c1 * pow(c2, 10 ** 9 + 5, 10 ** 9 + 7)
        print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()