def solve():
    N, S = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for s in range(S + 1):
            if dp[i][s]:
                dp[i + 1][s] = True
            if s - cards[i][0] >= 0 and dp[i][s - cards[i][0]]:
                dp[i + 1][s] = True
            if s - cards[i][1] >= 0 and dp[i][s - cards[i][1]]:
                dp[i + 1][s] = True
    if not dp[N][S]:
        print('No')
        return
    print('Yes')
    ans = []
    s = S
    for i in range(N - 1, -1, -1):
        if s - cards[i][0] >= 0 and dp[i][s - cards[i][0]]:
            ans.append('H')
            s -= cards[i][0]
        elif s - cards[i][1] >= 0 and dp[i][s - cards[i][1]]:
            ans.append('T')
            s -= cards[i][1]
        else:
            assert False
    print(''.join(reversed(ans)))
