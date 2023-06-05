def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j] - int(a[i][j] == "-"), dp[i][j + 1] - int(a[i][j] == "-"))
            else:
                dp[i][j] = min(dp[i + 1][j] + int(a[i][j] == "+"), dp[i][j + 1] + int(a[i][j] == "+"))
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] == 0:
        print("Draw")
    else:
        print("Aoki")
main()
