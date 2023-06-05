def main():
    n,m = map(int,input().split())
    a = [0 for i in range(n)]
    for i in range(m):
        a[int(input())] = 1
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1,n):
        if a[i] == 1:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[n-1])

if __name__ == '__main__':
    main()