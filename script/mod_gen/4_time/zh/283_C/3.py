def solve():
    s = input()
    n = len(s)
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(n):
        for j in range(i, n):
            if i == 0 and s[j] == '0':
                continue
            dp[j+1] = min(dp[j+1], dp[i] + 1)
            if j + 1 < n:
                dp[j+2] = min(dp[j+2], dp[i] + 1)
            if j + 2 < n:
                dp[j+3] = min(dp[j+3], dp[i] + 2)
    print(dp[n])

if __name__ == '__main__':
    solve()