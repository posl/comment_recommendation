def main():
    N = int(input())
    X = [0] * N
    T = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    dp = [[0] * 5 for _ in range(N)]
    for i in range(N):
        for j in range(5):
            if j == X[i]:
                dp[i][j] = dp[i-1][j] + A[i]
            else:
                dp[i][j] = dp[i-1][j]
        for j in range(5):
            if T[i] - 1 == T[i-1] and j == X[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][X[i]] + A[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
    print(max(dp[N-1]))

if __name__ == '__main__':
    main()