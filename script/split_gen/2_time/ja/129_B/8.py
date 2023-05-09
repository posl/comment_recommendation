def main():
    N = int(input())
    W = [int(i) for i in input().split()]
    W_sum = sum(W)
    W_sum_half = W_sum // 2
    dp = [[False] * (W_sum_half + 1) for i in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(W_sum_half + 1):
            if j < W[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j] or dp[i][j - W[i]]
    for j in range(W_sum_half, -1, -1):
        if dp[N][j]:
            print(W_sum - 2 * j)
            break
