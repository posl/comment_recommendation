def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort()
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 3
    dp[5] = 5
    for i in range(6, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5]
        dp[i] %= 998244353
    for l, r in LR:
        dp[l] -= dp[r + 1]
        dp[l] %= 998244353
    print(dp[1])
main()

if __name__ == '__main__':
    main()