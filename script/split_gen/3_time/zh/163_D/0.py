def solve(N, K):
    MOD = 10**9 + 7
    ans = 0
    for i in range(K, N+2):
        ans += N * i + 1 - i * (i-1) // 2
        ans %= MOD
    return ans
