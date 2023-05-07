def main():
    N = int(input())
    MOD = 998244353
    # dp[i][j][k] := i 桁目まで決めて、j = 0 ならば前の桁と同じであること、j = 1 ならば前の桁より 1 大きいこと、j = 2 ならば前の桁より 1 小さいこと、k = 0 ならば 0 で始まっていないこと、k = 1 ならば 0 で始まっていることとしたときの、条件を満たす整数の個数
    dp = [[[0] * 2 for _ in range(3)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(2):
                for d in range(1, 10):
                    nj = 0
                    if d == 9:
                        nj = 2
                    elif d == 1:
                        nj = 1
                    dp[i + 1][nj][k | (d == 0)] += dp[i][j][k]
                    dp[i + 1][nj][k | (d == 0)] %= MOD
    ans = 0
    for j in range(3):
        for k in range(2):
            ans += dp[N][j][k]
    ans %= MOD
    print(ans)
