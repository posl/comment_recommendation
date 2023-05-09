def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    dp = [[-1 for i in range(N+1)] for j in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            for k in range(M):
                if C[k] == j+1:
                    dp[i+1][C[k]] = max(dp[i+1][C[k]], dp[i][j] + Y[k])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + X[i])
    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[N][i])
    print(ans)

if __name__ == '__main__':
    main()