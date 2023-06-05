def main():
    n,x = map(int,input().split())
    coins = [list(map(int,input().split())) for _ in range(n)]
    coins.sort()
    #print(coins)
    dp = [[0]*(x+1) for _ in range(n+1)]
    #print(dp)
    dp[0][0] = 1
    for i in range(n):
        for j in range(x+1):
            if j-coins[i][0]>=0:
                dp[i+1][j] = dp[i][j] | dp[i+1][j-coins[i][0]]
            else:
                dp[i+1][j] = dp[i][j]
    if dp[-1][-1]:
        print('Yes')
    else:
        print('No')
main()
