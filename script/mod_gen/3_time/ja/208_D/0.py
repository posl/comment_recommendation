def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    INF = 10 ** 15
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(M):
        dp[A[i]][B[i]] = C[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dp[i][j] <= dp[i][k] + dp[k][j]:
                    ans += dp[i][j]
    print(ans)
main()

if __name__ == '__main__':
    main()