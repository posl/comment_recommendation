def main():
    # Get input here
    n, m = map(int, input().strip().split())
    a = [int(input()) for _ in range(m)]
    # Calculate the answer from input here
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i not in a:
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
            if i - 2 >= 0:
                dp[i] += dp[i - 2]
            dp[i] %= mod
    # Print the answer here
    print(dp[n])

if __name__ == '__main__':
    main()