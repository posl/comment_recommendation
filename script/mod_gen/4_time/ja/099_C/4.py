def main():
    n = int(input())
    # dp[i] := i円を引き出すのに必要な最小回数
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(1, 7):
            if i - j**2 >= 0:
                dp[i] = min(dp[i], dp[i - j**2] + 1)
            else:
                break
        for j in range(1, 7):
            if i - j**6 >= 0:
                dp[i] = min(dp[i], dp[i - j**6] + 1)
            else:
                break
    print(dp[n])

if __name__ == '__main__':
    main()