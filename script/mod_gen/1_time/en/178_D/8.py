def dp(s, n, m):
    if s < 0:
        return 0
    if n == 0:
        if s == 0:
            return 1
        else:
            return 0
    if m < 3:
        return 0
    if dp_table[s][n][m] != -1:
        return dp_table[s][n][m]
    dp_table[s][n][m] = dp(s-m, n-1, m) + dp(s, n, m-1)
    return dp_table[s][n][m]
s = int(input())
dp_table = [[[-1 for i in range(s+1)] for j in range(s+1)] for k in range(s+1)]
print(dp(s, s, s) % (10**9+7))
