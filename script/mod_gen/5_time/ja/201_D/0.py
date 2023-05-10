def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                continue
            if i == H-1:
                if A[i][j+1] == '+':
                    dp[i][j] = dp[i][j+1] - 1
                else:
                    dp[i][j] = dp[i][j+1] + 1
            elif j == W-1:
                if A[i+1][j] == '+':
                    dp[i][j] = dp[i+1][j] - 1
                else:
                    dp[i][j] = dp[i+1][j] + 1
            else:
                if A[i][j+1] == '+':
                    dp[i][j] = min(dp[i][j+1] - 1, dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j+1] + 1, dp[i+1][j])
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()