def main():
    # input
    N, M = map(int, input().split())
    As = [int(input()) for _ in range(M)]
    # compute
    """WRITE BELOW"""
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(N):
        if i not in As:
            dp[i+1] += dp[i]
            dp[i+1] %= 10**9 + 7
        if i+1 not in As:
            dp[i+2] += dp[i]
            dp[i+2] %= 10**9 + 7
    # output
    print(dp[-1])

if __name__ == '__main__':
    main()