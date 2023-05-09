def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if A[0][0] == '+' else -1
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                continue
            if i > 0:
                if dp[i - 1][j] > 0:
                    dp[i][j] = -1 if A[i][j] == '+' else 1
                else:
                    dp[i][j] = 1 if A[i][j] == '+' else -1
            if j > 0:
                if dp[i][j - 1] > 0:
                    dp[i][j] = -1 if A[i][j] == '+' else 1
                else:
                    dp[i][j] = 1 if A[i][j] == '+' else -1
    if dp[-1][-1] > 0:
        print('Takahashi')
    elif dp[-1][-1] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()