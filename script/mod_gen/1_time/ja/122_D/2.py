def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                dp[3][i][j][k] = 1
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    dp[3][i][j][k] = 0
                if i == 0 and j == 1 and k == 2:
                    dp[3][i][j][k] = 0
                if i == 1 and j == 0 and k == 2:
                    dp[3][i][j][k] = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    dp[3][i][j][k] = 0
                if i == 0 and j == 1 and k == 2:
                    dp[3][i][j][k] = 0
                if i == 1 and j == 0 and k == 2:
                    dp[3][i][j][k] = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    dp[3][i][j][k] = 0
                if i == 0 and j == 1 and k == 2:
                    dp[3][i][j][k] = 0
                if i == 1 and j == 0 and k == 2:
                    dp[3][i][j][k] = 0
    for n in range(4, N+1):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if (i ==

if __name__ == '__main__':
    main()