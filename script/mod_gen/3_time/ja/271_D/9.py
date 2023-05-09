def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    # dp[i][j] = i枚目までのカードでjを作れるか
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j - cards[i][0] >= 0 and dp[i][j - cards[i][0]]:
                dp[i + 1][j] = True
            if j - cards[i][1] >= 0 and dp[i][j - cards[i][1]]:
                dp[i + 1][j] = True
    if not dp[n][s]:
        print("No")
        return
    print("Yes")
    ans = ["" for _ in range(n)]
    i = n
    j = s
    while i > 0:
        if j - cards[i - 1][0] >= 0 and dp[i - 1][j - cards[i - 1][0]]:
            ans[i - 1] = "H"
            j -= cards[i - 1][0]
        else:
            ans[i - 1] = "T"
            j -= cards[i - 1][1]
        i -= 1
    print("".join(ans))

if __name__ == '__main__':
    main()