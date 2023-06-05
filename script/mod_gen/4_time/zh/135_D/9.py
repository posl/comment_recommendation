def main():
    S = input()
    N = len(S)
    MOD = 10**9+7
    # 10^5までの階乗を求めておく
    fac = [0] * (N+1)
    fac[0] = 1
    for i in range(N):
        fac[i+1] = fac[i] * (i+1) % MOD
    # 10^5までの逆元を求めておく
    inv = [0] * (N+1)
    inv[N] = pow(fac[N], MOD-2, MOD)
    for i in range(N, 0, -1):
        inv[i-1] = inv[i] * i % MOD
    # 10^5までのパスカルの三角形を求めておく
    C = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N+1):
        C[i][0] = C[i][i] = 1
        for j in range(1, i):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD
    # 13で割った余りが0, 5のものをそれぞれ求める
    dp = [0] * 13
    dp[0] = 1
    for i in range(N):
        ndp = [0] * 13
        for j in range(13):
            if S[i] == "?":
                for k in range(10):
                    ndp[(j*10+k)%13] += dp[j]
                    ndp[(j*10+k)%13] %= MOD
            else:
                k = int(S[i])
                ndp[(j*10+k)%13] += dp[j]
                ndp[(j*10+k)%13] %= MOD
        dp = ndp
    # 13で割った余りが0, 5のものをそれぞれ求める
    ans = 0
    for i in range(13):
        if i % 13 == 5:
            ans += dp[i]
            ans %= MOD
    print

if __name__ == '__main__':
    main()