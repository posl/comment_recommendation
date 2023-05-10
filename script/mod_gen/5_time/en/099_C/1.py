def main():
    N = int(input())
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    for i in range(1,N+1):
        for j in [1,6,36,216,1296,7776,46656,9,81,729,6561,59049]:
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i-j]+1)
    print(dp[N])

if __name__ == '__main__':
    main()