Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    mod = 998244353
    dp = [[0] * 10 for _ in range(n)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= mod
    print(sum(dp[n - 1]) % mod)

=======
Suggestion 2

def main():
    N = int(input())
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    mod = 998244353
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    print(sum(dp[N]) % mod)

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = 9
    dp[0][1] = 1
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] * 9 + dp[i-1][1] * 9
        dp[i][1] = dp[i-1][0] + dp[i-1][1]
        dp[i][0] %= MOD
        dp[i][1] %= MOD
    print((dp[N-1][0] + dp[N-1][1]) % MOD)

=======
Suggestion 4

def main():
    N = int(input())
    mod = 998244353
    dp = [[0]*(N+1) for _ in range(10)]
    for i in range(1,10):
        dp[i][1] = 1
    for j in range(2,N+1):
        for i in range(10):
            if i == 0:
                dp[i][j] = dp[i+1][j-1]
            elif i == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]
            dp[i][j] = dp[i][j] % mod
    print(sum(dp[i][N] for i in range(1,10)) % mod)

=======
Suggestion 5

def main():
    N = int(input())
    mod = 998244353
    dp = [[0] * (N + 1) for _ in range(10)]
    for i in range(1, 10):
        dp[i][1] = 1
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[j][i] = dp[1][i - 1]
            elif j == 9:
                dp[j][i] = dp[8][i - 1]
            else:
                dp[j][i] = (dp[j - 1][i - 1] + dp[j + 1][i - 1]) % mod
    print(sum(dp[i][N] for i in range(10)) % mod)

=======
Suggestion 6

def main():
    N = int(input())
    # dp[i][j] = i桁目まで見て、jで終わる数の個数
    dp = [[0 for _ in range(10)] for _ in range(N)]
    # 1桁目は1から9までの数が1通りずつある
    for i in range(10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][0] = dp[i-1][1]
            elif j == 9:
                dp[i][9] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N-1]) % 998244353)

=======
Suggestion 7

def main():
    N = int(input())

    # dp[i][j][k] := i 桁目まで決めたときに、
    # その桁の数が j であるような数の個数
    # k = 0 ならば前の桁との差が 1 以下であるような数
    # k = 1 ならばそうでない数
    dp = [[[0] * 2 for _ in range(10)] for _ in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(10):
            for k in range(2):
                for d in range(10):
                    if k == 0:
                        if abs(j - d) <= 1:
                            dp[i + 1][d][0] += dp[i][j][k]
                        else:
                            dp[i + 1][d][1] += dp[i][j][k]
                    else:
                        dp[i + 1][d][1] += dp[i][j][k]

    ans = 0
    for j in range(1, 10):
        ans += dp[N][j][0] + dp[N][j][1]

    print(ans % 998244353)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    mod = 998244353

    #dp[i][j][k] := i桁目までで条件を満たす数の個数で、i桁目はjで、i-1桁目との差はk
    dp = [[[0 for _ in range(3)] for _ in range(10)] for _ in range(N+1)]
    #初期化
    for i in range(1,10):
        dp[1][i][0] = 1
    for i in range(2,N+1):
        for j in range(10):
            for k in range(3):
                if j == 0:
                    dp[i][j][1] += dp[i-1][j+1][k]
                elif j == 9:
                    dp[i][j][1] += dp[i-1][j-1][k]
                else:
                    dp[i][j][0] += dp[i-1][j-1][k]
                    dp[i][j][2] += dp[i-1][j+1][k]
                dp[i][j][0] %= mod
                dp[i][j][1] %= mod
                dp[i][j][2] %= mod

    ans = 0
    for i in range(10):
        for j in range(3):
            ans += dp[N][i][j]
            ans %= mod
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())

    # dp[i][j][k] = i 桁目まで決めて、j=0: 0 が含まれる, j=1: 0 が含まれない, k=0: 1 が含まれる, k=1: 1 が含まれない
    dp = [[[0]*2 for _ in range(2)] for _ in range(N)]

    # 初期条件
    dp[0][0][0] = 1
    dp[0][1][0] = 8
    dp[0][1][1] = 1

    # DP
    for i in range(1, N):
        for j in range(2):
            for k in range(2):
                if j == 0:
                    dp[i][j][0] += dp[i-1][j][k]
                else:
                    dp[i][j][0] += dp[i-1][j][k]
                    dp[i][j][1] += dp[i-1][j][k]

                if k == 0:
                    dp[i][j][0] += dp[i-1][j][k]
                else:
                    dp[i][j][0] += dp[i-1][j][k]
                    dp[i][j][1] += dp[i-1][j][k]

    # 答え
    ans = dp[N-1][0][0] + dp[N-1][1][0] + dp[N-1][1][1]
    ans %= 998244353
    print(ans)
