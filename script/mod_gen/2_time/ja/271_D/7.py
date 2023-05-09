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
        for i in range(N, 0, -1):
            if dp[i - 1][S - A[i - 1][0]]:
                S -= A[i - 1][0]
                ans.append('H')
            else:
                S -= A[i - 1][1]
                ans.append('T')
        print(''.join(ans[::-1]))
    else:
        print('No')

if __name__ == '__main__':
    main()