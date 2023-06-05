def main():
    s = input()
    atcoder = 'atcoder'
    n = len(s)
    dp = [[n+1 for _ in range(8)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(8):
            if s[i] == atcoder[j]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
                if j < 7:
                    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + 1)
            else:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    if dp[n][7] == n+1:
        print(-1)
    else:
        print(n - dp[n][7])
