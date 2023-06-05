def main():
    s = input()
    atcoder = 'atcoder'
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(atcoder) + 1)]
    for i in range(1, len(atcoder) + 1):
        dp[i][0] = i
    for j in range(1, len(s) + 1):
        dp[0][j] = j
    for i in range(1, len(atcoder) + 1):
        for j in range(1, len(s) + 1):
            if atcoder[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    print(dp[len(atcoder)][len(s)])
