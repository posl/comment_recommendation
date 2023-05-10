def solve(N,K):
    MOD = 10**9+7
    ans = 0
    for i in range(K,N+2):
        ans += (N+1)*i - i*(i-1) + 1
        ans %= MOD
    return ans
