def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j] := i 番目までの弁当から選んで、たこ焼きを j 個以上食べられるかどうか
    # dp[i][j] = dp[i-1][j] or dp[i-1][j-A[i]]
    dp = [[False] * (X+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(1, N+1):
        for j in range(X+1):
            dp[i][j] = dp[i-1][j]
            if j - A[i-1] >= 0:
                dp[i][j] |= dp[i-1][j-A[i-1]]
    
    # dp2[i][j] := i 番目までの弁当から選んで、たい焼きを j 個以上食べられるかどうか
    # dp2[i][j] = dp2[i-1][j] or dp2[i-1][j-B[i]]
    dp2 = [[False] * (Y+1) for _ in range(N+1)]
    dp2[0][0] = True
    for i in range(1, N+1):
        for j in range(Y+1):
            dp2[i][j] = dp2[i-1][j]
            if j - B[i-1] >= 0:
                dp2[i][j] |= dp2[i-1][j-B[i-1]]
    # dp[i][j] = True かつ dp2[i][j] = True となる i, j の組み合わせのうち、
    # i + j が最小となるものを探す
    ans = 10**9
    for i in range(N+1):
        for j in range(X+1):
            if dp[i][j]

if __name__ == '__main__':
    main()