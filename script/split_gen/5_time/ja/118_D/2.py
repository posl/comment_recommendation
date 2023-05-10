def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(n):
        for j in a:
            if i+j <= n:
                dp[i+j] = max(dp[i+j],dp[i]*10+j)
    print(dp[n])
