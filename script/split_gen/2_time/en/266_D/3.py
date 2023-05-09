def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[[0] * 5 for _ in range(5)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            for k in range(5):
                if j != k:
                    dp[i + 1][k][X[i]] = max(dp[i + 1][k][X[i]], dp[i][j][k] + A[i])
                if T[i] >= abs(j - k):
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
    print(max([dp[N][j][k] for j in range(5) for k in range(5)]))
