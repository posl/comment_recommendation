def main():
    N,M = list(map(int,input().split()))
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    for i in range(1,N+1):
        if i in a:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()