def main():
    L = int(input())
    #L = 17
    dp = [0]*201
    dp[0] = 1
    for i in range(1, L+1):
        for j in range(1, L+1):
            if i - j >= 0:
                dp[i] += dp[i-j]
    print(dp[L])

if __name__ == '__main__':
    main()