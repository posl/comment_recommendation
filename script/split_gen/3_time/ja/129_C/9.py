def main():
    # 入力
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]
    # 1,000,000,007 で割った余りを出力することに注意して下さい。
    MOD = 10**9 + 7
    # 解答
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1,N+1):
        if i in A:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[N] % MOD)
