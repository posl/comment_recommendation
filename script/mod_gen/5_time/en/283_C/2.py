def solve():
    S = input()
    n = len(S)
    dp = [[float('inf') for i in range(2)] for j in range(n+1)]
    dp[n][0] = 0
    dp[n][1] = 1
    for i in range(n-1, -1, -1):
        s = int(S[i])
        for j in range(2):
            for k in range(10):
                if j == 1 and k == 0:
                    continue
                if dp[i][j] > dp[i+1][j] + k + (10-j)*s:
                    dp[i][j] = dp[i+1][j] + k + (10-j)*s
    print(dp[0][0])

if __name__ == '__main__':
    solve()