def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    # dp[i][j]はSのi文字目までから、chokudaiのj文字目までを選んだときの場合の数
    dp = [[0] * 9 for _ in range(n + 1)]
    # dpの初期値
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(n):
        for j in range(8):
            dp[i + 1][j + 1] += dp[i][j] if s[i] == "chokudai"[j] else 0
            dp[i + 1][j + 1] += dp[i][j + 1]
            dp[i + 1][j + 1] %= mod
    print(dp[n][8])

if __name__ == '__main__':
    main()