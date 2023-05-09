def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    for i in range(n - a + 1, n - b + 1):
        ans -= nCr(n, i)
    print(ans % mod)

if __name__ == '__main__':
    main()