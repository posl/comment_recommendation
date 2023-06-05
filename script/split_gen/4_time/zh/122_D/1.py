def main():
    N = int(input())
    MOD = 10**9+7
    #dp[i][j][k][l]表示长度为i，最后三个字符为jkl的字符串的数量。
    #jkl是0,1,2,3分别表示A,C,G,T。
    dp = [[[[0 for l in range(4)] for k in range(4)] for j in range(4)] for i in range(N+1)]
    #初始化
    #长度为0的字符串只有一种情况，就是空字符串。
    dp[0][3][3][3] = 1
    #动态规划
    for i in range(1,N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        #不允许出现AGC
                        if (k==0 and l==1 and m==2) or (k==0 and j==1 and m==2) or (j==0 and k==1 and m==2) or (k==0 and l==2 and m==1) or (k==2 and l==0 and m==1):
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= MOD
    #计算答案
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)
