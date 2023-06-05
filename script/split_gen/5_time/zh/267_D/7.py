def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,n+1):
        dp[1][i] = dp[1][i-1] + a[i-1]
    for i in range(2,m+1):
        for j in range(i,n+1):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+i*a[j-1])
    print(dp[m][n])
