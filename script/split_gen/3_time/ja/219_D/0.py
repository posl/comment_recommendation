def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for _ in range(X + Y + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, X + Y + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if j >= A[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - A[i - 1]] + B[i - 1])
            if j >= B[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - B[i - 1]] + A[i - 1])
    for i in range(X, X + Y + 1):
        if dp[N][i] >= X:
            print(i - X)
            return
    print(-1)
