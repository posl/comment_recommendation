def make_num(n, a):
    dp = [0]*(n+1)
    for i in range(n+1):
        for j in a:
            if i+j <= n:
                dp[i+j] = max(dp[i]+1, dp[i+j])
    return dp[n]

if __name__ == '__main__':
    make_num()