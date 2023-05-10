def main():
    import sys
    from collections import defaultdict
    from operator import mul
    from functools import reduce
    from itertools import combinations_with_replacement
    MOD = 998244353
    def ncr(n, r):
        if r > n:
            return 0
        r = min(r, n-r)
        numer = reduce(mul, range(n, n-r, -1), 1)
        denom = reduce(mul, range(1, r+1), 1)
        return (numer // denom) % MOD
    def ncr2(n, r):
        return fact[n] * factinv[r] * factinv[n-r] % MOD
    def ncr3(n, r):
        return fact[n] * inv(r) * inv(n-r) % MOD
    def inv(n):
        return pow(n, MOD-2, MOD)
    N, M, K = map(int, sys.stdin.readline().split())
    fact = [1] * (N+1)
    factinv = [1] * (N+1)
    for i in range(1, N+1):
        fact[i] = fact[i-1] * i % MOD
        factinv[i] = inv(fact[i])
    ans = 0
    for i in range(N+1):
        tmp = ncr3(N-1, i)
        tmp *= pow(M-1, N-i-1, MOD)
        tmp *= M
        tmp %= MOD
        ans += tmp
        ans %= MOD
    print(ans)
