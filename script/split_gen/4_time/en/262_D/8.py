def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = 998244353
    # 累積和
    # 累積和を作る
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    # 累積和の差の累積和
    T = [0] * (N+1)
    for i in range(N):
        T[i+1] = T[i] + S[i+1]
    # 累積和の差の累積和の差
    U = [0] * (N+1)
    for i in range(N):
        U[i+1] = U[i] + T[i+1]
    # dp[i][j] := i番目までの数を使ってj個選ぶときの場合の数
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(i+1):
            dp[i][j] += dp[i-1][j] * 2
            dp[i][j] %= mod
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] %= mod
    ans = 0
    for i in range(1,N+1):
        ans += dp[N][i] * U[i]
        ans %= mod
    print(ans)
