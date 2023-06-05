def main():
    n,x = map(int,input().split())
    a_b = [list(map(int,input().split())) for _ in range(n)]
    a_b.sort(key=lambda x:x[0])
    #print(a_b)
    dp = [[0]*(x+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(x+1):
            if j == 0:
                dp[i+1][j] = 1
            elif j >= a_b[i][0]:
                dp[i+1][j] = dp[i][j] or dp[i+1][j-a_b[i][0]]
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print('Yes' if dp[n][x] else 'No')
