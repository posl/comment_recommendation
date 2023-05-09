def main():
    N = int(input())
    mod = 998244353
    #dp[i][j][k] := i桁目まで見たとき、j=0:未満確定,1:未満未確定, k=0:差が1未満,1:差が1
    dp = [[[0]*2 for _ in range(2)] for _ in range(N+1)]
    dp[0][1][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(2):
                for l in range(10):
                    if j == 0 and l > 9:
                        continue
                    if k == 0 and l > 1:
                        continue
                    dp[i+1][j or l < 9][k or l == 1] += dp[i][j][k]
                    dp[i+1][j or l < 9][k or l == 1] %= mod
    print((sum(dp[N][0])+sum(dp[N][1]))%mod)

if __name__ == '__main__':
    main()