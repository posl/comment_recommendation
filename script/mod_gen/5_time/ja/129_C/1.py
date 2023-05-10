def main():
    N,M = map(int,input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    a.insert(0,0)
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if i in a:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N]%1000000007)

if __name__ == '__main__':
    main()