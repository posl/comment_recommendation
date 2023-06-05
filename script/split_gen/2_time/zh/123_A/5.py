def main():
    n = int(input())
    mod = 10**9+7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    #dp[3][a][b][c]表示最后三个字符是abc的字符串数
    #a,b,c表示最后三个字符的种类
    #a,b,c的取值范围为0,1,2,3
    #0:A,1:C,2:G,3:T
    #最后一个字符是A的字符串数
    dp[0][1][2][3] = 1
    dp[0][2][1][3] = 1
    dp[0][1][3][2] = 1
    for i in range(n-3):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        #最后三个字符是bcd，且不包含AGC
                        if not (b == 1 and c == 2 and d == 3) and not (b == 2 and c == 1 and d == 3) and not (b == 1 and c == 3 and d == 2):
                            dp[i+1][b][c][d] += dp[i][a][b][c]
                            dp[i+1][b][c][d] %= mod
    ans = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                ans += dp[n-3][a][b][c]
                ans %= mod
    print(ans)
