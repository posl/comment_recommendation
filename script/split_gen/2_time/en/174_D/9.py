def main():
    N = int(input())
    c = input()
    # 0: W, 1: R
    dp = [[0 for i in range(2)] for j in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    for i in range(N):
        if c[i] == 'W':
            dp[i+1][0] = dp[i][0] + 1
            dp[i+1][1] = min(dp[i][0], dp[i][1])
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = min(dp[i][0], dp[i][1]) + 1
    print(dp[N][1])
