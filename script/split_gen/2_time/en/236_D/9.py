def f(x, y):
    if x > y:
        return f(y, x)
    if y % x == 0:
        return x
    return f(y % x, x)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dp[i + 1][1 << i | 1 << j] = f(a[i][j], a[i][j])
for i in range(n):
    for j in range(1 << n):
        if not (j >> i & 1):
            continue
        for k in range(n):
            if i == k:
                continue
            if j >> k & 1:
                continue
            dp[k + 1][j | 1 << k] = max(dp[k + 1][j | 1 << k], dp[i + 1][j] ^ a[i][k])
print(dp[n][(1 << n) - 1])
