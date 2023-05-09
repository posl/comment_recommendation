def main():
    N = int(input())
    T = [0] * (N + 1)
    X = [0] * (N + 1)
    A = [0] * (N + 1)
    for i in range(N):
        T[i + 1], X[i + 1], A[i + 1] = map(int, input().split())
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if T[i + 1] - T[i] >= abs(X[i + 1] - j):
                dp[i + 1][X[i + 1]] = max(dp[i + 1][X[i + 1]], dp[i][j] + A[i + 1])
    print(max(dp[N]))

if __name__ == '__main__':
    main()