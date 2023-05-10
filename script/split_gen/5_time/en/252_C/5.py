def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 10**10
    for i in range(n):
        dp = [[10**10] * 10 for _ in range(n)]
        dp[0][i] = 0
        for j in range(1, n):
            for k in range(10):
                for l in range(10):
                    if s[j][l] == str(k):
                        dp[j][k] = min(dp[j][k], dp[j-1][l] + abs(l-k))
        ans = min(ans, min(dp[n-1]))
    print(ans)
