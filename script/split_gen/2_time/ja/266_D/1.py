def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            if j == X[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + A[i])
            if abs(j - X[i]) <= T[i + 1] - T[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][X[i]] + A[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(max(dp[-1]))
