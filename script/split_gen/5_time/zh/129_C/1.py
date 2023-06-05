def main():
    n,m = map(int,input().split())
    broken = [0] * (n+1)
    for i in range(m):
        broken[int(input())] = 1
    mod = 1000000007
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        if broken[i] == 1:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= mod
    print(dp[n])
