def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    dp = [[[False for _ in range(300 * 300 + 1)] for _ in range(300 + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(300):
            for k in range(300 * 300 + 1):
                if dp[i][j][k]:
                    dp[i + 1][j][k] = True
                    if j + 1 <= 300 and k + a[i] <= 300 * 300:
                        dp[i + 1][j + 1][k + a[i]] = True
    ans = -1
    for i in range(300 * 300 + 1):
        if dp[n][x][i] and dp[n][y][i]:
            ans = i
            break
    print(ans)
