def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) + 1 - l):
            dp = [0] * (N + 1)
            for i in range(l):
                dp[i + 1] = dp[i] + V[i]
            for i in range(r):
                dp[N - i - 1] = dp[N - i] + V[N - i - 1]
            dp[l + r] = dp[l] + dp[N - r]
            dp[l + r] += sum(sorted(V)[N - l - r:N - r])
            ans = max(ans, dp[l + r])
    print(ans)
