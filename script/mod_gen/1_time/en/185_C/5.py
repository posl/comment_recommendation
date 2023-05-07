def main():
    L = int(input())
    dp = [0] * (L+1)
    dp[0] = 1
    for i in range(1, L+1):
        for j in range(i, L+1):
            dp[j] += dp[j-i]
    print(dp[L])

if __name__ == '__main__':
    main()