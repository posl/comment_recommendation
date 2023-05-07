def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    # dp[i] = i番目のマスにたどり着く方法の数
    dp = [0] * (N + 1)
    dp[1] = 1
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]]
    # dp[i-LR[k][0]] = dp[i-LR[k][1]] + ... + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
    # dp[i] = dp[i-1] + ... + dp[i-LR[k][1]] - dp[i-LR[k][1]-LR[k][1]+LR[k][0]] + dp[i-LR[k][1]-LR[k][1]+LR[k][0]]
