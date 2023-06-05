def solve():
    n, w = map(int, input().split())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n):
        for j in range(w + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + B[i] <= w:
                dp[i + 1][j + B[i]] = max(dp[i + 1][j + B[i]], dp[i][j] + A[i] * B[i])
    print(dp[n][w])
solve()
