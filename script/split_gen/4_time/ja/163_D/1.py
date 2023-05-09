def solve():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        ans += (N-i+1)*i+1
        ans %= mod
    return ans
