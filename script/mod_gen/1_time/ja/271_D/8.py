def main():
    N, S = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + A[i][0] <= S:
                    dp[i + 1][j + A[i][0]] = True
                if j + A[i][1] <= S:
                    dp[i + 1][j + A[i][1]] = True
    if dp[N][S]:
        print('Yes')
        ans = []
        for i in reversed(range(N)):
            if S - A[i][0] >= 0 and dp[i][S - A[i][0]]:
                ans.append('H')
                S -= A[i][0]
            else:
                ans.append('T')
                S -= A[i][1]
        print(''.join(reversed(ans)))
    else:
        print('No')

if __name__ == '__main__':
    main()