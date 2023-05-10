def main():
    N = int(input())
    dp = [N] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for j in range(1, N + 1):
            if i + j ** 2 <= N:
                dp[i + j ** 2] = min(dp[i + j ** 2], dp[i] + 1)
    print(dp[N])

if __name__ == '__main__':
    main()