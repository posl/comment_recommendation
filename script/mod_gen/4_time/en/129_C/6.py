def main():
    N,M = map(int,input().split())
    a = [0]*N
    for i in range(M):
        a[int(input())-1] = 1
    dp = [0]*N
    dp[0] = 1
    for i in range(1,N):
        if a[i] == 1:
            dp[i] = 0
        else:
            if i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
    print(dp[N-1]%(10**9+7))

if __name__ == '__main__':
    main()