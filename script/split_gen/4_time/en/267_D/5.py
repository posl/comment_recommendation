def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [[-float('inf')]*(n+1) for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(1,m+1):
        for j in range(n+1):
            if j > 0:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+a[j-1]*i)
            dp[i][j] = max(dp[i][j],dp[i][j-1])
    print(dp[-1][-1])
