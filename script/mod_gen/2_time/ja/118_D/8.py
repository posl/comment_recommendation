def answer(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] < 0:
            continue
        for j in a:
            dp[i + j] = max(dp[i + j], dp[i] * 10 + j)
    return dp[n]

if __name__ == '__main__':
    answer()