def solve(n, k, v):
    ans = 0
    for i in range(1, k+1):
        for j in range(i+1):
            if j <= n and i-j <= n:
                dp = [[-10**9 for _ in range(i+1)] for _ in range(i+1)]
                dp[0][0] = 0
                for l in range(n):
                    if l != j-1 and l != n-(i-j):
                        for m in range(i+1):
                            if m != 0:
                                dp[l+1][m] = max(dp[l+1][m], dp[l][m-1]+v[l])
                            dp[l+1][m] = max(dp[l+1][m], dp[l][m])
                ans = max(ans, dp[n][i-j])
    return ans
n, k = map(int, input().split())
v = list(map(int, input().split()))
print(solve(n, k, v))
