def main():
    #输入
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(input()))
    #动态规划
    dp = [[0 for i in range(W)] for j in range(H)]
    dp[H-1][W-1] = 0
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                continue
            elif i == H-1:
                if A[i][j] == "+":
                    dp[i][j] = dp[i][j+1]-1
                else:
                    dp[i][j] = dp[i][j+1]+1
            elif j == W-1:
                if A[i][j] == "+":
                    dp[i][j] = dp[i+1][j]-1
                else:
                    dp[i][j] = dp[i+1][j]+1
            else:
                if A[i][j] == "+":
                    dp[i][j] = max(dp[i+1][j]-1,dp[i][j+1]-1)
                else:
                    dp[i][j] = min(dp[i+1][j]+1,dp[i][j+1]+1)
    #判断
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")
