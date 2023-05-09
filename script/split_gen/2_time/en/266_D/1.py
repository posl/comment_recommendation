def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0] * 5 for i in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if T[i] >= abs(X[i] - j):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][X[i]] + A[i])
    print(max(dp[N]))
main()
