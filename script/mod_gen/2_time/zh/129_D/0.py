def main():
    N,M = map(int,input().split())
    a = [int(input()) for _ in range(M)]
    dp = [0 for _ in range(N+1)]
    dp[0] = 1
    for i in range(N+1):
        for j in range(1,3):
            if i-j >= 0 and not(i-j in a):
                dp[i] += dp[i-j]
                dp[i] %= 1000000007
    print(dp[N])

if __name__ == '__main__':
    main()