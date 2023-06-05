def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    # 重量的范围是1~W，因此我们只需要考虑重量的和W以下的情况
    # 用dp[i]表示重量和为i的时候，最多可以选择多少个砝码
    # 用dp[i] = max(dp[i], dp[i - A[j]] + 1)来更新dp[i]
    # 由于我们最多只能选择3个砝码，因此我们只需要更新dp[i] 3次
    # 最后dp[W]就是答案
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + 1)
            if j - A[i] > 0:
                dp[j] = max(dp[j], dp[j - A[i]] + 1)
                if j - A[i] - A[i] > 0:
                    dp[j] = max(dp[j], dp[j - A[i] - A[i]] + 1)
    print(dp[W])
