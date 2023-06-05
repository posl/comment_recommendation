def problem281_d():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(n):
        for j in range(n,0,-1):
            if dp[j-1] == 1 and dp[j] == 0:
                if a[i] <= j*d:
                    dp[j] = 1
    ans = -1
    for i in range(n,0,-1):
        if dp[i] == 1:
            ans = i*d
            break
    print(ans)
problem281_d()
