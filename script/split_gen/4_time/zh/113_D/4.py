def main():
    h,w,k = map(int, input().split())
    if w == 1:
        print(1)
        return
    dp = [[0 for i in range(w)] for j in range(h+1)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if j == 0:
                dp[i+1][j] = (dp[i][j] * (2**(w-2))) % 1000000007
            elif j == w-1:
                dp[i+1][j] = (dp[i][j] * (2**(w-2))) % 1000000007
            else:
                dp[i+1][j] = (dp[i][j-1] * (2**(w-j-2)) * dp[i][j] * (2**(j-1))) % 1000000007
    print(dp[h][k-1])
