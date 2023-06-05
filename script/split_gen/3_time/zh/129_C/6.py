def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    mod = 1000000007
    # 一次性将所有台阶的情况列出来
    # dp[i] 代表到达第i个台阶的方法数
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    # 将不能踩的台阶置为0
    for i in range(M):
        dp[A[i]] = 0
    print(dp[N])
