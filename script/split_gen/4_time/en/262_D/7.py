def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] := i個の要素からなる部分集合のうち、和がjになるものの個数
    dp = [[0] * (sum(A) + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sum(A) + 1):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j] %= MOD
            if j + A[i] <= sum(A):
                dp[i + 1][j + A[i]] += dp[i][j]
                dp[i + 1][j + A[i]] %= MOD
    ans = 0
    for i in range(1, sum(A) + 1):
        if i % N == 0:
            ans += dp[N][i]
            ans %= MOD
    print(ans)
