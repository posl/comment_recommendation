def main():
    n, s = map(int, input().split())
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a[i] <= s:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= s:
                    dp[i + 1][j + b[i]] = True
    if dp[n][s]:
        print("Yes")
        ans = ""
        for i in range(n - 1, -1, -1):
            if dp[i][s - a[i]]:
                ans += "H"
                s -= a[i]
            else:
                ans += "T"
                s -= b[i]
        ans = ans[::-1]
        print(ans)
    else:
        print("No")
