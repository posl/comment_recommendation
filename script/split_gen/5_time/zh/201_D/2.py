def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i == h - 1 and j == w - 1:
                continue
            if (i + j) % 2 == 0:
                if i == h - 1:
                    dp[i][j] = dp[i][j + 1]
                elif j == w - 1:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
            else:
                if i == h - 1:
                    dp[i][j] = dp[i][j + 1] - int(a[i][j + 1] == "+")
                elif j == w - 1:
                    dp[i][j] = dp[i + 1][j] - int(a[i + 1][j] == "+")
                else:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) - int(a[i][j + 1] == "+") + int(a[i + 1][j] == "+")
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] == 0:
        print("Draw")
    else:
        print("Aoki")
