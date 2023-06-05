def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #dp[i][j] 表示前i个数，最后一个数为j的方案数
    dp = [[0 for i in range(10)] for j in range(N+1)]
    #初始化
    dp[0][A[0]] = 1
    #状态转移
    for i in range(1, N):
        for j in range(10):
            #F
            #print(i, j, A[i])
            dp[i][(j+A[i])%10] += dp[i-1][j]
            dp[i][(j+A[i])%10] %= 998244353
            #G
            dp[i][(j*A[i])%10] += dp[i-1][j]
            dp[i][(j*A[i])%10] %= 998244353
    #print(dp)
    #输出结果
    for i in range(10):
        print(dp[N-1][i])
