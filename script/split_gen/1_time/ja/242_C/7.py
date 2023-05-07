def main():
    N = int(input())
    # dp[i][j][k] := i 桁目まで決めて、j=0: 未満フラグが立っていない、j=1: 未満フラグが立っている
    #                 かつ、k=0: 1 で始まっていない、k=1: 1 で始まっている
    #                 といった状態で、条件を満たす整数の個数
    dp = [[[0] * 2 for _ in range(2)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(2):
                for x in range(1, 10):
                    ni = i + 1
                    nj = j
                    nk = k
                    if x != 1:
                        nk = 1
                    if j == 0:
                        if x < 9:
                            nj = 1
                    else:
                        if x == 9:
                            continue
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= 998244353
    ans = 0
    for j in range(2):
        for k in range(2):
            ans += dp[N][j][k]
            ans %= 998244353
    print(ans)
