def main():
    n, s = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + cards[i][0] <= s:
                    dp[i + 1][j + cards[i][0]] = True
                if j + cards[i][1] <= s:
                    dp[i + 1][j + cards[i][1]] = True
    if not dp[n][s]:
        print('No')
    else:
        print('Yes')
        ans = ''
        for i in range(n - 1, 0, -1):
            if dp[i][s] and dp[i - 1][s]:
                ans += 'T'
            elif dp[i][s - cards[i][0]] and dp[i - 1][s - cards[i][0]]:
                ans += 'H'
                s -= cards[i][0]
            else:
                ans += 'H'
                s -= cards[i][1]
        if s == cards[0][0]:
            ans += 'H'
        else:
            ans += 'T'
        print(ans[::-1])
