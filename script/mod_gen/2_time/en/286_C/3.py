def solve():
    n,a,b = map(int,input().split())
    s = input()
    dp = [float('inf')]*n
    dp[0] = a
    for i in range(1,n):
        dp[i] = min(dp[i], dp[i-1]+a)
        for j in range(1,i+1):
            if s[i-j] == s[i]:
                dp[i] = min(dp[i], dp[i-j-1]+b)
    print(dp[-1])

if __name__ == '__main__':
    solve()