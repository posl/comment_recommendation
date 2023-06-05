def main():
    #输入
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #处理
    ans = 10**18
    for _ in range(2):
        dp = [[10**18]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+C)
                ans = min(ans, dp[i][j]+A[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

if __name__ == '__main__':
    main()