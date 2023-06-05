def solve(h, w, a):
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j] - a[i + 1][j], dp[i][j + 1] - a[i][j + 1])
            else:
                dp[i][j] = max(dp[i + 1][j] + a[i + 1][j], dp[i][j + 1] + a[i][j + 1])
    if dp[0][0] > 0:
        return 'Takahashi'
    elif dp[0][0] < 0:
        return 'Aoki'
    else:
        return 'Draw'
h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
a = [[1 if a[i][j] == '+' else -1 for j in range(w)] for i in range(h)]
print(solve(h, w, a))
