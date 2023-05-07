def main():
    L = int(input())
    dp = [1] + [0] * (L - 1)
    for i in range(2, L + 1):
        for j in range(i, L + 1):
            dp[j] += dp[j - i]
    print(dp[L] - 1)

if __name__ == '__main__':
    main()