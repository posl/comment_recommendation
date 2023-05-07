def main():
    N, S = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            dp[i + 1][j] = dp[i][j] or dp[i][j - A[i][0]] or dp[i][j - A[i][1]]
    if dp[N][S]:
        print('Yes')
        ans = []
        j = S
        for i in range(N, 0, -1):
            if dp[i - 1][j - A[i - 1][0]]:
                ans.append('H')
                j -= A[i - 1][0]
            elif dp[i - 1][j - A[i - 1][1]]:
                ans.append('T')
                j -= A[i - 1][1]
            else:
                ans.append('H')
        print(''.join(ans[::-1]))
    else:
        print('No')

if __name__ == '__main__':
    main()