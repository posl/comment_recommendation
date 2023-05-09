def comb(n, r, mod):
    if r > n:
        return 0
    return fact[n] * factinv[r] * factinv[n-r] % mod
mod = 10**9+7
N = int(input())
C = list(map(int, input().split()))
