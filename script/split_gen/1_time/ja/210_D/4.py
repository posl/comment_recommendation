def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * (W + 1) for _ in range(H + 1)]
        for i in range(H):
            for j in range(W):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + C
                ans = min(ans, dp[i + 1][j + 1] + A[i][j])
        A.reverse()
    print(ans)
