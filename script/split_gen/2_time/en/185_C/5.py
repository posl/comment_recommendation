def main():
    L = int(input())
    dp = [[0 for i in range(L+1)] for j in range(L+1)]
    for i in range(1,L+1):
        dp[1][i] = 1
    for i in range(2,L+1):
        for j in range(1,L+1):
            for k in range(1,j-i+2):
                dp[i][j] += dp[i-1][j-k]
    print(dp[L][L])
