def main():
    S = input()
    if S[0] == 'o':
        dp = [[0, 0] for _ in range(4)]
        dp[0] = [1, 0]
    elif S[0] == 'x':
        dp = [[0, 0] for _ in range(4)]
        dp[0] = [0, 1]
    else:
        dp = [[0, 0] for _ in range(4)]
        dp[0] = [1, 1]
    for i in range(1, 4):
        if S[i] == 'o':
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][1]
        elif S[i] == 'x':
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0] + dp[i-1][1]
    print(dp[-1][0] * 10 + dp[-1][1] * 9)

if __name__ == '__main__':
    main()