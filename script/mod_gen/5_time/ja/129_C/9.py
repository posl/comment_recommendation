def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]
    a.append(N+1)
    mod = 1000000007
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if i == a[j]:
                dp[i] = 0
                break
            if i == 1:
                dp[i] = 1
                continue
            if i == 2:
                dp[i] = 2
                continue
            if i == 3:
                dp[i] = 3
                continue
            dp[i] = (dp[i-1] + dp[i-2])%mod
    print(dp[N])

if __name__ == '__main__':
    main()