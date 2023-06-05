def solve(n, w, a):
    a.sort()
    dp = [0] * (w + 1)
    for i in range(n):
        for j in range(w + 1):
            if j >= a[i]:
                dp[j] = max(dp[j], dp[j - a[i]] + a[i])
    return dp[w]

if __name__ == '__main__':
    solve()