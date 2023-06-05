def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = [[0 for _ in range(1001)] for _ in range(1001)]
    for i in range(n):
        for j in range(1000, -1, -1):
            if j >= c[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]] + v[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][1000])
