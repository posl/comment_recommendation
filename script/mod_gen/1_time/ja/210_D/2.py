def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18 for _ in range(W)] for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                ans = min(ans, A[i][j] + C * (i+j) + dp[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

if __name__ == '__main__':
    main()