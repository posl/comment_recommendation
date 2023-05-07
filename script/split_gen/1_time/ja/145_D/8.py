def main():
    X, Y = map(int, input().split())
    MOD = 10 ** 9 + 7
    # 1 <= X <= 10^6
    # 1 <= Y <= 10^6
    # 1 <= i <= X
    # 1 <= j <= Y
    # dp[i][j] = (i, j) にナイトの駒を移動させる方法の数
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 1
    for i in range(X + 1):
        for j in range(Y + 1):
            if i + 1 <= X and j + 2 <= Y:
                dp[i + 1][j + 2] += dp[i][j]
                dp[i + 1][j + 2] %= MOD
            if i + 2 <= X and j + 1 <= Y:
                dp[i + 2][j + 1] += dp[i][j]
                dp[i + 2][j + 1] %= MOD
    print(dp[X][Y])
