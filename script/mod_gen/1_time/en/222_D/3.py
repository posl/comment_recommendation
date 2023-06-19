def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i][j] = (dp[i - 1][j - 1] * (B[i - 1] - j + 1) + dp[i - 1][j] * (j - A[i - 1])) % mod
    print(sum(dp[N]) % mod)
solve()
