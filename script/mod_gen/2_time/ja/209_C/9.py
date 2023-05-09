def main():
    n = int(input())
    c = list(map(int, input().split()))
    #print(n)
    #print(c)
    #print(len(c))
    #print(c[0])
    #print(c[-1])
    #dp = [[0] * (n+1) for i in range(n+1)]
    dp = [0] * (n+1)
    #print(dp)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % (10**9+7)
    #print(dp)
    ans = 1
    for i in range(n):
        if i == 0:
            ans *= dp[c[i]-1]
        else:
            if c[i] == c[i-1]:
                ans *= dp[c[i]-1] - dp[c[i]-2]
            else:
                ans *= dp[c[i]-1]
        ans = ans % (10**9+7)
    print(ans)

if __name__ == '__main__':
    main()