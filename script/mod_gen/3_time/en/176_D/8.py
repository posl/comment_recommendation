def main():
    H,W=map(int,input().split())
    CH,CW=map(int,input().split())
    DH,DW=map(int,input().split())
    S=[input() for i in range(H)]
    INF=10**9
    dp=[[INF]*W for i in range(H)]
    dp[CH-1][CW-1]=0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                continue
            for k in range(-2,3):
                for l in range(-2,3):
                    if 0<=i+k<H and 0<=j+l<W and S[i+k][j+l]=="." and dp[i+k][j+l]>dp[i][j]+(abs(k)+abs(l)>1):
                        dp[i+k][j+l]=dp[i][j]+(abs(k)+abs(l)>1)
    if dp[DH-1][DW-1]==INF:
        print(-1)
    else:
        print(dp[DH-1][DW-1])

if __name__ == '__main__':
    main()