def solve(N, A):
    mod = 998244353
    ans = 0
    for i in range(N):
        ans += A[i]
    ans *= pow(2, N-1, mod)
    ans %= mod
    return ans
