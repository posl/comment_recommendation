def main():
    N, M, K = map(int, input().split())
    #dp[i][j][k] := i番目までの数列でj個の数を使って和がkになる場合の数
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                if j+1 <= M and k+i+1 <= K:
                    dp[i+1][j+1][k+i+1] += dp[i][j][k]
                    dp[i+1][j+1][k+i+1] %= 998244353
                if k+i+1 <= K:
                    dp[i+1][j][k+i+1] += dp[i][j][k]*(j+1)
                    dp[i+1][j][k+i+1] %= 998244353
    print(dp[N][M][K])
