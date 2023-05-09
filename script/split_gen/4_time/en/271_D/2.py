def main():
    N, S = map(int, input().split())
    cards = []
    for _ in range(N):
        a, b = map(int, input().split())
        cards.append((a, b))
    dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + cards[i][0] <= S:
                    dp[i + 1][j + cards[i][0]] = True
                if j + cards[i][1] <= S:
                    dp[i + 1][j + cards[i][1]] = True
    if not dp[N][S]:
        print('No')
    else:
        print('Yes')
        ans = ''
        for i in reversed(range(N)):
            if S - cards[i][0] >= 0 and dp[i][S - cards[i][0]]:
                ans += 'T'
                S -= cards[i][0]
            else:
                ans += 'H'
                S -= cards[i][1]
        print(ans[::-1])
