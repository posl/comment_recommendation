def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    dp = [[0]*2**n for _ in range(n+1)]
    for i in range(n):
        for j in range(2**(n-i-1)):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j*2] + a[i][i+1+j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j*2] + a[i][i+1+j])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j*2+1] + a[i][i+1+j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j*2+1] + a[i][i+1+j])
    print(dp[n][1])
