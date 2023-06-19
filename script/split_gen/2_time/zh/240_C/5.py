def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    dp = [[False] * (x + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x + 1):
            if dp[i][j]:
                dp[i + 1][j + a[i]] = True
                dp[i + 1][j + b[i]] = True
    print("Yes" if dp[n][x] else "No")
