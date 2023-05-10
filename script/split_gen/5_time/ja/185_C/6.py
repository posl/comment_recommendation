def solve():
    n = int(input())
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = sum(dp[:i-2])+1
    print(dp[n])
