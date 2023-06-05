def solve():
    s = input()
    t = "atcoder"
    ls = len(s)
    lt = len(t)
    dp = [[0 for i in range(lt+1)] for j in range(ls+1)]
    for i in range(ls+1):
        dp[i][0] = i
    for i in range(lt+1):
        dp[0][i] = i
    for i in range(1,ls+1):
        for j in range(1,lt+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
    print(dp[ls][lt])
solve()
