def main():
    a,b,k = map(int,input().split())
    s = a+b
    dp = [[0]*(b+1) for i in range(a+1)]
    dp[0][0] = 1
    for i in range(a+1):
        for j in range(b+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ""
    while a > 0 and b > 0:
        if dp[a-1][b] >= k:
            ans += "a"
            a -= 1
        else:
            ans += "b"
            k -= dp[a-1][b]
            b -= 1
    while a > 0:
        ans += "a"
        a -= 1
    while b > 0:
        ans += "b"
        b -= 1
    print(ans)
