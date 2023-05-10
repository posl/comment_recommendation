def solve():
    N, S = map(int, input().split())
    ab = []
    for _ in range(N):
        a, b = map(int, input().split())
        ab.append((a, b))
    dp = [[0 for _ in range(S + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j] == 0:
                continue
            if j + ab[i][0] <= S:
                dp[i + 1][j + ab[i][0]] = 1
            if j + ab[i][1] <= S:
                dp[i + 1][j + ab[i][1]] = 1
    if dp[N][S] == 0:
        print('No')
        return
    print('Yes')
    ans = ''
    for i in range(N - 1, -1, -1):
        if S - ab[i][0] >= 0 and dp[i][S - ab[i][0]] == 1:
            ans += 'T'
            S -= ab[i][0]
        else:
            ans += 'H'
            S -= ab[i][1]
    print(ans[::-1])

if __name__ == '__main__':
    solve()