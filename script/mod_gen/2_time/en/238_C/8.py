def f(n):
    if n < 10: return n
    k = len(str(n))
    return 9 * pow(10, k - 2, MOD) + f(n % pow(10, k - 1))
MOD = 998244353
N = int(input())
print((f(N) + f(N + 1)) % MOD)
