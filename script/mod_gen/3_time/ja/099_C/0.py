def main():
    n = int(input())
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        six = 1
        while i-6**six >= 0:
            dp[i] = min(dp[i], dp[i-6**six] + 1)
            six += 1
        nine = 1
        while i-9**nine >= 0:
            dp[i] = min(dp[i], dp[i-9**nine] + 1)
            nine += 1
    print(dp[-1])

if __name__ == '__main__':
    main()