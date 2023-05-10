def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for j in range(3001)] for i in range(n)]
    for i in range(a[0], b[0]+1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(a[i], b[i]+1):
            dp[i][j] = sum(dp[i-1][a[i-1]:j+1]) % mod
    print(sum(dp[n-1]) % mod)
    return
