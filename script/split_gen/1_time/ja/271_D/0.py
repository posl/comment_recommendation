def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - a[i] >= 0:
                dp[i + 1][j] |= dp[i][j - a[i]]
            if j - b[i] >= 0:
                dp[i + 1][j] |= dp[i][j - b[i]]
    if dp[N][S]:
        ans = []
        j = S
        for i in range(N, 0, -1):
            if j - a[i - 1] >= 0 and dp[i - 1][j - a[i - 1]]:
                ans.append('H')
                j -= a[i - 1]
            else:
                ans.append('T')
                j -= b[i - 1]
        print('Yes')
        print(''.join(ans[::-1]))
    else:
        print('No')
