def solve():
    N, S = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # dp[i][j] = (i番目までのカードを使って、表をjにすることができるか)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + AB[i][0] <= S:
                    dp[i + 1][j + AB[i][0]] = True
                if j + AB[i][1] <= S:
                    dp[i + 1][j + AB[i][1]] = True
    if dp[N][S]:
        ans = []
        for i in range(N - 1, 0, -1):
            if S - AB[i][0] >= 0 and dp[i][S - AB[i][0]]:
                ans.append('H')
                S -= AB[i][0]
            else:
                ans.append('T')
                S -= AB[i][1]
        ans.reverse()
        ans.append('H' if S == AB[0][0] else 'T')
        print(''.join(ans))
    else:
        print('No')
