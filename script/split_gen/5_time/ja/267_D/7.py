def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    #dp[i][j] := i番目までの要素からj個選んだときの最大値
    dp = [[-float('inf')]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j == 0:
                dp[i+1][j] = 0
            else:
                if i >= 1:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                if i >= 1:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j-1]+a[i])
    print(max(dp[-1]))
