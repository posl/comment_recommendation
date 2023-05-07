def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        for j in range(2, 6):
            if i >= 6**j:
                dp[i] = min(dp[i], dp[i-6**j] + 1)
            else:
                break
        for j in range(2, 6):
            if i >= 9**j:
                dp[i] = min(dp[i], dp[i-9**j] + 1)
            else:
                break
    print(dp[N])
main()

if __name__ == '__main__':
    main()