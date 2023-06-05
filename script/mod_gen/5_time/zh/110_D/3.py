def solve(n, m):
    # write code here
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, j + 1):
                if j % k == 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % 1000000007
    res = 0
    for i in range(1, m + 1):
        res = (res + dp[n][i]) % 1000000007
    return res
while True:
    try:
        n, m = map(int, input().split())
        print(solve(n, m))
    except:
        break

if __name__ == '__main__':
    solve()