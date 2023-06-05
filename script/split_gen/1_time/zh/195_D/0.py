def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        ans = 0
        for i in range(M):
            if i < L or R < i:
                ans += X[i]
        dp = [0] * (sum(X) + 1)
        for i in range(N):
            for j in range(sum(X), W[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])
        ans += dp[sum(X)]
        print(ans)
