def main():
    n, x = map(int, input().split())
    coins = [list(map(int, input().split())) for _ in range(n)]
    coins.sort(key=lambda x: x[0])
    dp = [[0 for _ in range(x + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(x + 1):
            for k in range(coins[i][1] + 1):
                if j + coins[i][0] * k <= x:
                    dp[i + 1][j + coins[i][0] * k] += dp[i][j]
    print("Yes" if dp[n][x] > 0 else "No")
