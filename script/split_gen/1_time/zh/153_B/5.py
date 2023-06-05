def solve():
    # 读入输入
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 用于动态规划的数组，dp[i]表示减少i点生命值所需的最小消耗
    dp = [float("inf")] * (H + 1)
    dp[0] = 0
    for i in range(H + 1):
        for j in range(N):
            # 注意判断是否越界
            if i + A[j] <= H:
                dp[i + A[j]] = min(dp[i + A[j]], dp[i] + 1)
            else:
                dp[H] = min(dp[H], dp[i] + 1)
    if dp[H] <= 1:
        print("Yes")
    else:
        print("No")
