def main():
    # 读取输入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 用来组成数字1，2，3，4，5，6，7，8，9的火柴棒数量
    B = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    # 从大到小排序
    A.sort(reverse=True)
    # 从小到大排序
    # A.sort()
    # dp[i]表示用i根火柴棒所能形成的最大整数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i >= B[A[j] - 1] and dp[i - B[A[j] - 1]] != -1:
                dp[i] = max(dp[i], dp[i - B[A[j] - 1]] * 10 + A[j])
    print(dp[N])
