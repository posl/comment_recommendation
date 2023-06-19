def main():
    #读取输入
    N = int(input())
    #定义DP
    #dp[i][j]表示长度为i，最高位为j的满足条件的数的个数
    dp = [[0 for i in range(10)] for i in range(N+1)]
    #初始化
    for i in range(1,10):
        dp[1][i] = 1
    #dp
    for i in range(2,N+1):
        for j in range(10):
            #最高位为j
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j-1]
            dp[i][j] = dp[i][j] % 998244353
    #计算答案
    answer = 0
    for i in range(10):
        answer = answer + dp[N][i]
        answer = answer % 998244353
    #输出
    print(answer)
