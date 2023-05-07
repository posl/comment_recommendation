def main():
    n,s = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int, input().split())
    dp = [[False]*(s+1) for i in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s+1):
            if j-a[i]>=0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-a[i]]
            if j-b[i]>=0:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-b[i]]
    if dp[n][s]:
        print('Yes')
        ans = ''
        i = n
        j = s
        while i>0:
            if j-a[i-1]>=0 and dp[i-1][j-a[i-1]]:
                ans += 'H'
                j -= a[i-1]
            else:
                ans += 'T'
                j -= b[i-1]
            i -= 1
        print(ans[::-1])
    else:
        print('No')
