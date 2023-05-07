def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3001):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
            if A[i] <= j <= B[i]:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
    print(dp[N][3000])
