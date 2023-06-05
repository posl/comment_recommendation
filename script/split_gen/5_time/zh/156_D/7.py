def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    ans = pow(2, n, mod) - 1
    c = 1
    for i in range(a):
        c *= n - i
        c %= mod
        c *= pow(a - i, mod - 2, mod)
        c %= mod
    for i in range(b):
        c *= n - i
        c %= mod
        c *= pow(b - i, mod - 2, mod)
        c %= mod
    ans -= c
    ans %= mod
    print(ans)
