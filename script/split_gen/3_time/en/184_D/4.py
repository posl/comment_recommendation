def main():
    A, B, C = map(int, input().split())
    # A, B, C = 31, 41, 59
    # A, B, C = 0, 0, 1
    # A, B, C = 98, 99, 99
    # A, B, C = 99, 99, 99
    N = A + B + C
    prob = [A/N, B/N, C/N]
    dp = [[0]*(N+1) for _ in range(3)]
    for i in range(3):
        for j in range(N+1):
            if i == 0:
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + dp[i][j-1]
            else:
                if j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = prob[i]*dp[i][j-1] + prob[i-1]*dp[i-1][j]
    print(dp[2][N])
