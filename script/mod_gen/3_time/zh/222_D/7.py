def solve(n, a, b):
    # dp[i][j] 表示第i位为j时的数量
    dp = [[0 for j in range(3001)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(a[i-1], b[i-1]+1):
            if i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = sum(dp[i-1][a[i-2]:j+1]) % 998244353
    return sum(dp[n]) % 998244353
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
