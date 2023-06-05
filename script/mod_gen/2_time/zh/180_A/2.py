def main():
    # 读入数据
    N, K = map(int, input().split())
    # 读入K个区间
    # 区间按照左端点排序
    intervals = []
    for i in range(K):
        L, R = map(int, input().split())
        intervals.append((L, R))
    intervals.sort()
    # dp[i]表示到达i的方案数
    dp = [0] * (N+1)
    dp[1] = 1
    # 遍历区间
    for i in range(K):
        L, R = intervals[i]
        # 计算区间[L, R]的方案数
        # 从左到右遍历每个位置
        # 如果当前位置是区间的左端点，那么它的方案数就是dp[L]
        # 如果当前位置不是区间的左端点，那么它的方案数就是dp[L] + dp[L+1] + ... + dp[R]
        # 为了防止重复计算，我们可以用一个数组sum存储dp[L] + dp[L+1] + ... + dp[R]的值
        # 令sum[i] = dp[L] + dp[L+1] + ... + dp[i]
        # 那么sum[i+1] = sum[i] + dp[i+1]
        # 这样我们就可以用sum[R] - sum[L-1]来计算区间[L, R]的方案数
        sum = [0] * (N+1)
        sum[0] = dp[0]
        for j in range(1, N+1):
            sum[j] = sum[j-1] + dp[j]
        # 计算区间[L, R]的方案数
        # sum[R] - sum[L-1]
        dp[L] = sum[R] - sum[L-1]
        # 防止dp[L]为负数
        dp[L] %= 998244353
        # 更新dp
        for j in range(L+1, R+1):
            dp[j] = 0
    # 打印结果

if __name__ == '__main__':
    main()