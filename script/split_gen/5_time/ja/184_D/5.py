def main():
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        print(0)
        return
    if a == 0 or b == 0 or c == 0:
        print(100)
        return
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    dp[a][b][c] = 1
    for i in range(a,100):
        for j in range(b,100):
            for k in range(c,100):
                if i == 0 and j == 0 and k == 0:
                    continue
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 100
                    continue
                dp[i][j][k] = (dp[i+1][j][k]*i + dp[i][j+1][k]*j + dp[i][j][k+1]*k) / (i+j+k) + 1
    print(dp[a][b][c])
    return
