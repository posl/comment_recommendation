def main():
    # 读入数据
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    # 从后往前，计算每个时刻能抓到的最大值
    # dp[i]表示从第i个时刻到第N个时刻，能抓到的最大值
    # dp[i] = max(dp[i+1], dp[i+1] - (T[i+1] - T[i]) + A[i+1])
    dp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        dp[i] = max(dp[i+1], dp[i+1] - (T[i+1] - T[i]) + A[i+1])
    # 从前往后，计算每个时刻能抓到的最大值
    # dp[i]表示从第0个时刻到第i个时刻，能抓到的最大值
    # dp[i] = max(dp[i-1], dp[i-1] - (T[i] - T[i-1]) + A[i])
    for i in range(1, N+1):
        dp[i] = max(dp[i-1], dp[i-1] - (T[i] - T[i-1]) + A[i])
    # 打印结果
    print(dp[N])
    return

if __name__ == '__main__':
    main()