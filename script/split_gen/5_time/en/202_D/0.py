def main():
    a, b, k = map(int, input().split())
    n = a + b
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(b + 1):
            if j == 0:
                dp[i + 1][j] = dp[i][j + 1]
            elif j == b:
                dp[i + 1][j] = dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j + 1]
    res = ""
    while a > 0 and b > 0:
        if k > dp[a + b - 1][b - 1]:
            res += "b"
            k -= dp[a + b - 1][b - 1]
            b -= 1
        else:
            res += "a"
            a -= 1
    res += "a" * a + "b" * b
    print(res)
    return
