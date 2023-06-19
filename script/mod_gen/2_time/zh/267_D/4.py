def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[-float('inf') for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+(i+1)*a[j])
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1][j])
    print(dp[m][n])

if __name__ == '__main__':
    main()