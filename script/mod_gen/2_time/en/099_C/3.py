def main():
    n = int(input())
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(6):
            if i - 6**j >= 0:
                dp[i] = min(dp[i], dp[i-6**j] + 1)
        for j in range(9):
            if i - 9**j >= 0:
                dp[i] = min(dp[i], dp[i-9**j] + 1)
    print(dp[n])

if __name__ == '__main__':
    main()