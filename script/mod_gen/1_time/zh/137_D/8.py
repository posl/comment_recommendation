def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照结束时间从小到大排序
    ab.sort(key=lambda x: x[0])
    # 从今天开始，一共可以工作的天数
    t = m + 1
    # dp[i][j]表示从第i个工作开始，一共工作了j天所能获得的最大奖励
    dp = [[0] * t for _ in range(n + 1)]
    # 从最后一个工作开始
    for i in range(n - 1, -1, -1):
        # 从第i个工作开始，最多可以工作的天数
        for j in range(t):
            # 从第i个工作开始，工作j天所能获得的最大奖励
            # 1.如果第i个工作的结束时间超过了总天数，那么第i个工作不能接受，所以从第i+1个工作开始工作j天所能获得的最大奖励就是从第i+1个工作开始工作j天所能获得的最大奖励
            # 2.如果第i个工作的结束时间没有超过总天数，那么第i个工作可以接受，所以从第i个工作开始工作j天所能获得的最大奖励就是从第i+1个工作开始工作j+1天所能获得的最大奖励加上第i个工作的奖励
            if ab[i][0] + j > m:
                dp[i][j] = dp[i + 1][j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1] + ab[i][1])
    print(dp[0][0])

if __name__ == '__main__':
    main()