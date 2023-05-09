def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    for _ in range(2):
        dp = [[float('inf')] * (W + 1) for _ in range(H + 1)]
        for i in range(H):
            for j in range(W):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + C
                ans = min(ans, dp[i + 1][j + 1] + A[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

if __name__ == '__main__':
    main()