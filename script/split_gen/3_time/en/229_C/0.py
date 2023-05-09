def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0] * (W + 1) for i in range(N + 1)]
    for i in range(N):
        for w in range(W + 1):
            if w - B[i] >= 0:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - B[i]] + A[i])
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
    print(dp[N][W])
