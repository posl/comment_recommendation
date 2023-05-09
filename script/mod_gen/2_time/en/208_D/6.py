def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**18
    dp = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][i] = 0
    for i in range(M):
        a, b, c = ABC[i]
        dp[a][b] = c
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    ans += dp[i][k] + dp[k][j]
                    dp[i][j] = dp[i][k] + dp[k][j]
    print(ans)

if __name__ == '__main__':
    main()