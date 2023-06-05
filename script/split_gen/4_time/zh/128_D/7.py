def solve(n, k, v):
    ans = 0
    for i in range(0, k+1):
        for j in range(0, k+1):
            if i+j > n:
                continue
            dp = [[0 for x in range(n+1)] for y in range(k+1)]
            for l in range(0, k+1):
                for m in range(0, n+1):
                    if l == 0 and m == 0:
                        continue
                    dp[l][m] = -float('inf')
                    if m > 0 and l > 0:
                        dp[l][m] = max(dp[l][m], dp[l-1][m-1] + v[i+l-1])
                    if m > 0 and i+j-l > 0:
                        dp[l][m] = max(dp[l][m], dp[l][m-1] + v[i+j-l-1])
                    if m > 0 and j > 0:
                        dp[l][m] = max(dp[l][m], dp[l][m-1])
                    if m > 0:
                        dp[l][m] = max(dp[l][m], dp[l][m-1])
                    if l > 0:
                        dp[l][m] = max(dp[l][m], dp[l-1][m])
            ans = max(ans, dp[k][n])
    return ans
