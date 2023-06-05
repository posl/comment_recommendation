def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(10)]
        for a in range(10):
            for b in range(10):
                dp[(a + b) % 10][b] += 1
                dp[a][(a * b) % 10] += 1
        for a in range(10):
            for b in range(10):
                dp[a][b] %= mod
        for a in range(N - 1):
            for b in range(10):
                dp[(A[a] + b) % 10][b] += dp[A[a]][b]
                dp[A[a]][(A[a] * b) % 10] += dp[A[a]][b]
                dp[(A[a] + b) % 10][b] %= mod
                dp[A[a]][(A[a] * b) % 10] %= mod
        ans[i] = dp[A[-1]][i]
    print(*ans, sep='\n')
solve()
