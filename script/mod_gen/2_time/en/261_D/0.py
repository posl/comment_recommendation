def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N + 1):
            if dp[i][j] > dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j]
            if j > 0 and dp[i][j - 1] + X[i] > dp[i + 1][j]:
                dp[i + 1][j] = dp[i][j - 1] + X[i]
            for k in range(M):
                if j >= C[k] and dp[i][j - C[k]] + X[i] + Y[k] > dp[i + 1][j]:
                    dp[i + 1][j] = dp[i][j - C[k]] + X[i] + Y[k]
    print(dp[N][N])

if __name__ == '__main__':
    main()