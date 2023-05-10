def main():
    h,w = map(int,input().split())
    a = [input() for i in range(h)]
    #print(a)
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[-1][-1] = 1 if a[-1][-1] == '+' else -1
    for i in range(h-2,-1,-1):
        if a[i][-1] == '+':
            dp[i][-1] = dp[i+1][-1] - 1
        else:
            dp[i][-1] = dp[i+1][-1] + 1
    for i in range(w-2,-1,-1):
        if a[-1][i] == '+':
            dp[-1][i] = dp[-1][i+1] - 1
        else:
            dp[-1][i] = dp[-1][i+1] + 1
    #print(dp)
    for i in range(h-2,-1,-1):
        for j in range(w-2,-1,-1):
            if a[i][j] == '+':
                dp[i][j] = max(dp[i+1][j] - 1, dp[i][j+1] - 1)
            else:
                dp[i][j] = min(dp[i+1][j] + 1, dp[i][j+1] + 1)
    #print(dp)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()