def main():
    x, y = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
    dp[0][0] = 1
    for i in range(x+1):
        for j in range(y+1):
            if i + 1 <= x and j + 2 <= y:
                dp[i+1][j+2] += dp[i][j]
                dp[i+1][j+2] %= mod
            if i + 2 <= x and j + 1 <= y:
                dp[i+2][j+1] += dp[i][j]
                dp[i+2][j+1] %= mod
    print(dp[x][y])
