def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[[0 for _ in range(10)] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i][A[i]] = 1
    for i in range(N):
        for j in range(N-i-1):
            for k in range(10):
                dp[j][j+i+1][(k+A[j+i+1])%10] += dp[j][j+i][k]
                dp[j][j+i+1][(k*A[j+i+1])%10] += dp[j][j+i][k]
                dp[j][j+i+1][k] %= 998244353
    for i in range(10):
        print(dp[0][N-1][i]%998244353)
