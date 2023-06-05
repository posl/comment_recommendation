def main():
    # 读取输入
    X, Y = map(int, input().split())
    # 初始化
    MOD = 1000000007
    dp = [[0 for i in range(Y + 1)] for j in range(X + 1)]
    dp[0][0] = 1
    # 递推
    for i in range(X + 1):
        for j in range(Y + 1):
            if i + 1 <= X and j + 2 <= Y:
                dp[i + 1][j + 2] += dp[i][j]
            if i + 2 <= X and j + 1 <= Y:
                dp[i + 2][j + 1] += dp[i][j]
    # 打印
    print(dp[X][Y] % MOD)
