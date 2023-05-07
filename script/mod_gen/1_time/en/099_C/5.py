def main():
    N = int(input())
    coins = [1]
    for i in range(1, 6):
        coins.append(6**i)
        coins.append(9**i)
    coins.sort()
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    print(dp[N])

if __name__ == '__main__':
    main()