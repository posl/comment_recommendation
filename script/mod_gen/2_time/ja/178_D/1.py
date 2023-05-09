def main():
    S = int(input())
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(3, S + 1):
        for j in range(i, S + 1):
            dp[j] = (dp[j] + dp[j - i]) % (10 ** 9 + 7)
    print(dp[S])

if __name__ == '__main__':
    main()