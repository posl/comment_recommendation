def solve():
    s = input()
    atcoder = 'atcoder'
    n = len(s)
    dp = [[0]*(n+1) for _ in range(8)]
    for i in range(8):
        for j in range(n):
            if i == 0:
                dp[i][j+1] = dp[i][j] + 1
            elif atcoder[i] != s[j]:
                dp[i][j+1] = dp[i][j]
            else:
                dp[i][j+1] = min(dp[i-1][j], dp[i][j]) + 1
    print(dp[-1][-1])
solve()

if __name__ == '__main__':
    solve()