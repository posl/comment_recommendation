def main():
    s = input()
    mod = 10**9+7
    #dp[i][j] = i文字目まで見たときに、j文字目に何を入れるかの場合の数
    #dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    #dp[i-1][j-1] = 3文字目にAを入れる
    #dp[i-1][j] = 3文字目にBを入れる
    #dp[i-1][j+1] = 3文字目にCを入れる
    #dp[0][0] = 1
    dp = [[0]*4 for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(4):
            if s[i] == '?':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            elif j == 1 and s[i] == 'A':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            elif j == 2 and s[i] == 'B':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            elif j == 3 and s[i] == 'C':
                dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1]
            else:
                dp[i+1][j] = dp[i][j]
            dp[i+1][j] %= mod
    print(dp[len(s)][2])
