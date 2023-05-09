def main():
    N, M, K = map(int, input().split())
    # dp[i][j][k] := i番目までの整数からなる数列のうち、条件を満たすものの個数
    # j: 1~Mの整数
    # k: 1~Kの整数
    dp = [[[0] * (K+1) for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M):
            for k in range(K+1):
                # i番目までの整数からなる数列のうち、条件を満たすものの個数
                # に、i番目にj+1を追加したものを加える
                dp[i+1][j+1][k+j+1] += dp[i][j+1][k]
                dp[i+1][j+1][k+j+1] %= 998244353
                # i番目までの整数からなる数列のうち、条件を満たすものの個数
                # に、i番目にj+1を追加しなかったものを加える
                dp[i+1][j+1][k] += dp[i][j+1][k]
                dp[i+1][j+1][k] %= 998244353
    ans = 0
    for i in range(M+1):
        ans += dp[N][i][K]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()