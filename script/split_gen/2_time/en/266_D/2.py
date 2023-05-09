def main():
    N = int(input())
    T, X, A = [], [], []
    for _ in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    # dp[i][j] = i番目までのスヌークを捕まえたときの、座標jでの最大のスヌークの総和
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + A[i] (j == X[i])
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) (j != X[i])
    dp = [[0] * 5 for _ in range(N)]
    dp[0][X[0]] = A[0]
    for i in range(1, N):
        for j in range(5):
            if j == X[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + A[i]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
    print(max(dp[N-1]))
