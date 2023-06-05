def main():
    n = int(input())
    t = list(map(int, input().split()))
    # 递归
    # def f(i, x, y):
    #     if i == n:
    #         return max(x, y)
    #     return min(f(i + 1, x + t[i], y), f(i + 1, x, y + t[i]))
    # print(f(0, 0, 0))
    # 动态规划
    # dp = [[float('inf')] * (sum(t) + 1) for _ in range(n + 1)]
    # dp[0][0] = 0
    # for i in range(n):
    #     for j in range(sum(t) + 1):
    #         if j < t[i]:
    #             dp[i + 1][j] = dp[i][j]
    #         else:
    #             dp[i + 1][j] = min(dp[i][j - t[i]] + t[i], dp[i][j])
    # print(max(dp[n]))
    # 动态规划
    dp = [float('inf')] * (sum(t) + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(sum(t) + 1):
            if j < t[i]:
                continue
            dp[j] = min(dp[j - t[i]] + t[i], dp[j])
    print(max(dp))

if __name__ == '__main__':
    main()