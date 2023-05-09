def main():
    L = int(input())
    dp = [0] * (L+1)
    dp[0] = 1
    for i in range(L):
        for j in range(1, 12):
            if i+j <= L:
                dp[i+j] += dp[i]
    return dp[L]

if __name__ == '__main__':
    main()