def main():
    h,w,k = map(int,input().split())
    dp = [[[0]*w for _ in range(h+1)] for _ in range(w)]
    dp[0][0][0] = 1
    for i in range(h):
        for j in range(w):
            for k in range(2**(w-1)):
                for l in range(w-1):
                    if k & (1<<l):
                        if l-1>=0 and k & (1<<(l-1)):
                            dp[j][i+1][l-1] += dp[j][i][l]
                            dp[j][i+1][l-1] %= 1000000007
                        elif l+1<w-1 and k & (1<<(l+1)):
                            dp[j][i+1][l+1] += dp[j][i][l]
                            dp[j][i+1][l+1] %= 1000000007
                        else:
                            dp[j+1][i+1][l] += dp[j][i][l]
                            dp[j+1][i+1][l] %= 1000000007
                    else:
                        dp[j][i+1][l] += dp[j][i][l]
                        dp[j][i+1][l] %= 1000000007
    print(dp[k-1][h][0])
main()
