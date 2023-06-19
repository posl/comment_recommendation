def solve(n, s, a, b):
    dp = [[False for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j < a[i] and j < b[i]:
                dp[i+1][j] = False
            elif j < a[i]:
                dp[i+1][j] = dp[i][j-b[i]]
            elif j < b[i]:
                dp[i+1][j] = dp[i][j-a[i]]
            else:
                dp[i+1][j] = dp[i][j-a[i]] or dp[i][j-b[i]]
    if dp[n][s]:
        print("Yes")
        res = ""
        for i in range(n, 0, -1):
            if s >= a[i-1] and dp[i-1][s-a[i-1]]:
                res = "H" + res
                s -= a[i-1]
            else:
                res = "T" + res
                s -= b[i-1]
        print(res)
    else:
        print("No")

if __name__ == '__main__':
    solve()