def main():
    N = int(input())
    dp = [10000000000000] * (N + 1)
    dp[0] = 0
    for i in range(N):
        for j in range(1, 10):
            if i + j ** 6 <= N:
                dp[i + j ** 6] = min(dp[i + j ** 6], dp[i] + 1)
            if i + j ** 9 <= N:
                dp[i + j ** 9] = min(dp[i + j ** 9], dp[i] + 1)
    print(dp[N])

if __name__ == '__main__':
    main()