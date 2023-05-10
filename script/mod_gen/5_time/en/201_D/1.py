def solve():
    h, w = map(int, input().split())
    a = [list(input()) for i in range(h)]
    dp = [[0] * w for i in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if (i + j) % 2 == 0:
                if i == h-1 and j == w-1:
                    continue
                dp[i][j] = -10**18
                if i < h-1:
                    dp[i][j] = max(dp[i][j], dp[i+1][j] + (1 if a[i+1][j] == '+' else -1))
                if j < w-1:
                    dp[i][j] = max(dp[i][j], dp[i][j+1] + (1 if a[i][j+1] == '+' else -1))
            else:
                if i == h-1 and j == w-1:
                    continue
                dp[i][j] = 10**18
                if i < h-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] - (1 if a[i+1][j] == '+' else -1))
                if j < w-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] - (1 if a[i][j+1] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
solve()

if __name__ == '__main__':
    solve()