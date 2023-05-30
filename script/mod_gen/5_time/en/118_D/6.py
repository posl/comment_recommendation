def solve(N, M, A):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for a in A:
            if i >= a:
                dp[i] = max(dp[i], dp[i - a] * 10 + a)
    return dp[N]
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))
