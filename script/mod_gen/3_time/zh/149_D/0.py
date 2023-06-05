def solve():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    score = {'r': p, 's': r, 'p': s}
    win = {'r': 'p', 's': 'r', 'p': 's'}
    dp = [[0] * 3 for _ in range(n + 1)]
    for i in range(n):
        for j in range(3):
            if i >= k and win[t[i]] == win[t[i - k]] and j == win[t[i]]:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + score[win[t[i]]])
    print(max(dp[n]))
solve()
