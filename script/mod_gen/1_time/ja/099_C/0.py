def main():
    n = int(input())
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(1, 7):
            if 6 ** j > i:
                break
            dp[i] = min(dp[i], dp[i - 6 ** j] + 1)
        for j in range(1, 5):
            if 9 ** j > i:
                break
            dp[i] = min(dp[i], dp[i - 9 ** j] + 1)
    print(dp[n])

if __name__ == '__main__':
    main()