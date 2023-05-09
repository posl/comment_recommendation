def solve():
    n, s = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(s + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + ab[i][0] <= s:
                    dp[i + 1][j + ab[i][0]] = True
                if j + ab[i][1] <= s:
                    dp[i + 1][j + ab[i][1]] = True
    if not dp[n][s]:
        print('No')
        return
    ans = []
    for i in reversed(range(n)):
        if s - ab[i][0] >= 0 and dp[i][s - ab[i][0]]:
            ans.append('T')
            s -= ab[i][0]
        else:
            ans.append('H')
            s -= ab[i][1]
    print('Yes')
    print(''.join(ans[::-1]))
