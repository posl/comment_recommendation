def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    ans = pow(2, n, MOD) - 1
    c, d = 1, 1
    for i in range(b):
        c *= n - i
        c %= MOD
        d *= i + 1
        d %= MOD
    ans -= c * pow(d, MOD - 2, MOD)
    c, d = 1, 1
    for i in range(a):
        c *= n - i
        c %= MOD
        d *= i + 1
        d %= MOD
    ans -= c * pow(d, MOD - 2, MOD)
    ans %= MOD
    print(ans)
