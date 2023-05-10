def combination(n, r):
    if n < r:
        return 0
    else:
        x = 1
        y = 1
        for i in range(r):
            x = x * (n - i) % MOD
            y = y * (i + 1) % MOD
        return x * pow(y, MOD - 2, MOD) % MOD
MOD = 10 ** 9 + 7
X, Y = map(int, input().split())

if __name__ == '__main__':
    combination()