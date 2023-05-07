def main():
    s = input()
    mod = 10**9 + 7
    #文字列の長さ
    n = len(s)
    #dp[i][j] = i文字目まで見て、j文字目までの文字列を作ることができる場合の数
    dp = [[0] * 9 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(9):
            if j == 8:
                #最後の文字を作成した場合
                dp[i+1][j] = dp[i][j]
            elif s[i] == "c":
                #cを作成する場合
                dp[i+1][j] = dp[i][j]
            elif s[i] == "h" and j == 1:
                #hを作成する場合
                dp[i+1][j] = dp[i][j-1]
            elif s[i] == "o" and j == 2:
                #oを作成する場合
                dp[i+1][j] = dp[i][j-1]
            elif s[i] == "k" and j == 3:
                #kを作成する場合
                dp[i+1][j] = dp[i][j-1]
            elif s[i] == "u" and j == 4:
                #uを作成する場合
                dp[i+1][j] = dp[i][j-1]
            elif s[i] == "d" and j == 5:
                #dを作成する場合
                dp[i+1][j] = dp[i][j-1]
            elif s[i] == "a" and j == 6:
                #aを作成する場合
                dp[i+1][j] = dp[i][j-1]
            elif s[i] == "i" and j == 7:
                #iを作成する場合
                dp[i+1][j] = dp[i][j-1]
            else:
                #それ以外
                dp[i+1][j] = 0
            dp[i+1][j] %= mod

if __name__ == '__main__':
    main()