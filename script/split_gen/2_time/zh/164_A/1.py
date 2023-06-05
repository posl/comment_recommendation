def solve(n, k):
    MOD = 10**9 + 7
    ans = 0
    for i in range(k, n+2):
        ans += i * (n-i+1) + 1
        ans %= MOD
    return ans
