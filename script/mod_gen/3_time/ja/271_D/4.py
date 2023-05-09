def main():
    N, S = map(int, input().split())
    a = [None] * N
    b = [None] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + a[i] <= S:
                    dp[i + 1][j + a[i]] = True
                if j + b[i] <= S:
                    dp[i + 1][j + b[i]] = True
    if dp[N][S]:
        print('Yes')
        ans = [None] * N
        for i in range(N, 0, -1):
            if S - a[i - 1] >= 0 and dp[i - 1][S - a[i - 1]]:
                ans[i - 1] = 'H'
                S -= a[i - 1]
            else:
                ans[i - 1] = 'T'
                S -= b[i - 1]
        print(''.join(ans))
    else:
        print('No')

if __name__ == '__main__':
    main()