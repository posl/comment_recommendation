def problems286_c():
    N, A, B = map(int, input().split())
    S = input()
    T = S[::-1]
    dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N+1):
        for j in range(N+1):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + A)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + A)
            if i > 0 and j > 0:
                if S[i-1] == T[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + B)
    print(dp[N][N])

if __name__ == '__main__':
    problems286_c()