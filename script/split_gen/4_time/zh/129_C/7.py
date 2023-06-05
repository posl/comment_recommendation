def main():
    n,m = map(int,input().split())
    a = [int(input()) for _ in range(m)]
    a.append(n+1)
    mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(m+1):
            if i+1 == a[j]:
                dp[i] = 0
            elif i+1 > a[j]:
                dp[i] = (dp[i] + dp[i-a[j]-1]) % mod
    print(dp[n])
