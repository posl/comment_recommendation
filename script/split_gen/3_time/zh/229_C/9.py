def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_sum = sum(A)
    dp = [[0 for i in range(max_sum + 1)] for j in range(N + 1)]
    for i in range(N):
        for j in range(max_sum + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - A[i]] + B[i])
            else:
                dp[i + 1][j] = dp[i][j]
    ans = 0
    for i in range(max_sum + 1):
        if dp[N][i] <= W:
            ans = i
    print(ans)
solve()
