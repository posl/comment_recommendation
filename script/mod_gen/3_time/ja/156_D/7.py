def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    def calc(n, r):
        if n < r:
            return 0
        if n - r < r:
            r = n - r
        res = 1
        for i in range(r):
            res = res * (n - i) % MOD
        for i in range(r):
            res = res * pow(i + 1, MOD - 2, MOD) % MOD
        return res
    ans = pow(2, n, MOD) - 1 - calc(n, a) - calc(n, b)
    print(ans % MOD)

if __name__ == '__main__':
    main()