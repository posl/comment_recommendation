def main():
    A,B,C = map(int,input().split())
    p = [A/(A+B+C),B/(A+B+C),C/(A+B+C)]
    dp = [[0]*(101) for _ in range(101)]
    for i in range(1,101):
        for j in range(101):
            dp[i][j] = (i*p[0]+j*p[1]+(100-i-j)*p[2]+dp[i-1][j]+dp[i][j-1])/100
    print(dp[100][100])
