def main():
    n, m = map(int, input().split())
    broken = [int(input()) for _ in range(m)]
    # 1. 一次爬1阶或2阶，爬到第i阶的方法数记为dp[i]
    # 2. 如果第i阶是坏的，则dp[i] = 0
    # 3. 如果第i阶不是坏的，则dp[i] = dp[i-1] + dp[i-2]
    # 4. 边界条件：dp[0] = 1, dp[1] = 1, dp[2] = 2
    # 1. 一次爬1阶或2阶，爬到第i阶的方法数记为dp[i]
    dp = [0] * (n + 1)
    # 2. 如果第i阶是坏的，则dp[i] = 0
    for b in broken:
        dp[b] = -1
    # 4. 边界条件：dp[0] = 1, dp[1] = 1, dp[2] = 2
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    # 3. 如果第i阶不是坏的，则dp[i] = dp[i-1] + dp[i-2]
    for i in range(3, n + 1):
        if dp[i] != -1:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[n])

if __name__ == '__main__':
    main()