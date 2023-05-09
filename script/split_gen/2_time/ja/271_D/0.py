def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[0] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S + 1):
            if j - a[i] >= 0 and dp[i][j - a[i]] == 1:
                dp[i + 1][j] = 1
            if j - b[i] >= 0 and dp[i][j - b[i]] == 1:
                dp[i + 1][j] = 1
    if dp[N][S] == 0:
        print('No')
        return
    print('Yes')
    ans = []
    for i in range(N):
        if dp[N - i - 1][S - a[N - i - 1]] == 1:
            ans.append('H')
            S -= a[N - i - 1]
        else:
            ans.append('T')
            S -= b[N - i - 1]
    print(''.join(ans))
