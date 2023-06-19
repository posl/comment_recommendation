def problems129_c():
    n,m = map(int,input().split())
    a = [0]
    for i in range(m):
        a.append(int(input()))
    a.append(n+1)
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]
        for j in range(1,m+1):
            if a[j] == i:
                dp[i] = 0
                break
            elif a[j] > i:
                break
            else:
                dp[i] = (dp[i]+dp[i-a[j]-1])%1000000007
    print(dp[n])
