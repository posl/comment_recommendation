def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 if a[0][0] == "+" else -1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if (i + j) % 2 == 0:
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + (1 if a[i][j] == "+" else -1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + (1 if a[i][j] == "+" else -1)
                else:
                    dp[i][j] = max(dp[i][j - 1] + (1 if a[i][j] == "+" else -1), dp[i - 1][j] + (1 if a[i][j] == "+" else -1))
            else:
                if i == 0:
                    dp[i][j] = dp[i][j - 1] - (1 if a[i][j] == "+" else -1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] - (1 if a[i][j] == "+" else -1)
                else:
                    dp[i][j] = min(dp[i][j - 1] - (1 if a[i][j] == "+" else -1), dp[i - 1][j] - (1 if a[i][j] == "+" else -1))
    if dp[h - 1][w - 1] > 0:
        print("Takahashi")
    elif dp[h - 1][w - 1] < 0:
        print("Aoki")
    else:
        print("Draw")
