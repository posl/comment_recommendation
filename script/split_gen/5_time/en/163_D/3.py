def solve(n, k):
    mod = 10**9+7
    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1)*i+1
        ans %= mod
    return ans
