def main():
    n,m = map(int,input().split())
    a = [0]
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%1000000007)
