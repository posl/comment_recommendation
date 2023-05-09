def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    # dp[i][j] = i 番目までの弁当を買って、たこ焼きを j 個以上食べられるかどうか
    dp = [[False] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X + Y + 1):
            # i 番目の弁当を買わない場合
            if dp[i][j]:
                dp[i + 1][j] = True
            # i 番目の弁当を買う場合
            if j >= A[i] and dp[i][j - A[i]]:
                dp[i + 1][j] = True
            if j >= B[i] and dp[i][j - B[i]]:
                dp[i + 1][j] = True
    #print(dp)
    for i in range(X, X + Y + 1):
        if dp[N][i]:
            print(i - X)
            exit()
    print(-1)

if __name__ == '__main__':
    main()