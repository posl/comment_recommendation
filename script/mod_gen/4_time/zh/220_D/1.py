def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(N + 1)]
        dp[0][0] = 1
        for j in range(N):
            for k in range(10):
                dp[j + 1][(k + A[j]) % 10] += dp[j][k]
                dp[j + 1][(k + A[j]) % 10] %= MOD
                dp[j + 1][(k * A[j]) % 10] += dp[j][k]
                dp[j + 1][(k * A[j]) % 10] %= MOD
        ans[i] = dp[N][i]
    print(*ans, sep="\n")
solve()
