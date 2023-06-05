def solve():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[h-1][w-1] = 0
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if (i+j)%2 == 0:
                if i == h-1:
                    dp[i][j] = dp[i][j+1]
                elif j == w-1:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
            else:
                if i == h-1:
                    dp[i][j] = dp[i][j+1]
                elif j == w-1:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1])
            if a[i][j] == '+':
                dp[i][j] += 1
            else:
                dp[i][j] -= 1
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
