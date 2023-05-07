def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #dp[i][j] = i番目までのスヌークを見て、時間がjのときに取れる最大のスコア
    dp = [[0] * (T[N - 1] + 1) for i in range(N + 1)]
    for i in range(N):
        for j in range(T[i] + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + abs(X[i] - j) <= T[i]:
                dp[i + 1][X[i]] = max(dp[i + 1][X[i]], dp[i][j] + A[i])
    print(max(dp[N]))
