def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j - B[i] >= 0:
                dp[i + 1][j] = max(dp[i][j - B[i]] + A[i], dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])
