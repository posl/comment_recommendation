def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    keta = 0
    while k > 0:
        keta += 1
        k //= 2
    keta += 1
    #print(keta)
    keta = min(keta, 200000)
    #print(keta)
    dp = [[0 for _ in range(keta)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = a[i]-1
    for i in range(1,keta):
        for j in range(n):
            dp[j][i] = dp[dp[j][i-1]][i-1]
    #print(dp)
    ans = 0
    for i in range(keta):
        if (k >> i) & 1:
            ans = dp[ans][i]
    print(ans+1)
