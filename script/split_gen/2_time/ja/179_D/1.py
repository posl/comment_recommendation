def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    # dp[i] = iにたどり着く方法の数
    dp = [0] * (N+1)
    dp[1] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for k in range(K):
            li = i - R[k]
            ri = i - L[k]
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li-1]
            dp[i] %= 998244353
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= 998244353
    print(dp[N])
