def main():
    h,w = map(int,input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h)[::-1]:
        for j in range(w)[::-1]:
            if i == h-1 and j == w-1:
                continue
            if (i+j)%2 == 0:
                dp[i][j] = -float('inf')
                if i+1 < h:
                    dp[i][j] = max(dp[i][j],dp[i+1][j]+(1 if a[i+1][j] == '+' else -1))
                if j+1 < w:
                    dp[i][j] = max(dp[i][j],dp[i][j+1]+(1 if a[i][j+1] == '+' else -1))
            else:
                dp[i][j] = float('inf')
                if i+1 < h:
                    dp[i][j] = min(dp[i][j],dp[i+1][j]-(1 if a[i+1][j] == '+' else -1))
                if j+1 < w:
                    dp[i][j] = min(dp[i][j],dp[i][j+1]-(1 if a[i][j+1] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')
