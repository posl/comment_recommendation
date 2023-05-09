def dp(s, n):
    if s == 0:
        return 1
    if s < 0:
        return 0
    if n < 3:
        return 0
    if dp_table[s][n] != -1:
        return dp_table[s][n]
    dp_table[s][n] = dp(s - n, n) + dp(s, n - 1)
    return dp_table[s][n]
