Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1] % mod
            elif j == 9:
                dp[i][j] = dp[i-1][j-1] % mod
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    print(sum(dp[N]) % mod)

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(10):
                ni = i + 1
                nj = j
                if k == 0:
                    nj = 1
                if k == 9:
                    nj = 1
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= MOD
    print((dp[N][0] + dp[N][1]) % MOD)

=======
Suggestion 3

def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[0] * 2 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        dp[i+1][0] = (dp[i][0] * 8 + dp[i][1] * 9) % mod
        dp[i+1][1] = (dp[i][0] + dp[i][1] * 10) % mod
    print((dp[N][0] + dp[N][1]) % mod)

=======
Suggestion 4

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    MOD = 10 ** 9 + 7
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= MOD
    print((dp[N] * 2) % MOD)
    return

=======
Suggestion 5

def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = 0
    for i in range(1,N+1):
        ans += pow(10,i,MOD) - pow(9,i,MOD) - pow(9,i,MOD) + pow(8,i,MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = 0
    for i in range(N+1):
        ans += pow(10, i, MOD) * pow(9, N-i, MOD) * pow(8, i, MOD)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    import sys
    N = int(sys.stdin.readline())
    MOD = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    dp[1] = [1]*10
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD
    print(sum(dp[N])%MOD)

=======
Suggestion 8

def main():
    n = int(input())
    mod = 10**9 + 7
    ans = 0
    for i in range(1,n+1):
        ans += (10**i - 9**i - 9**i + 8**i)
    print(ans%mod)

=======
Suggestion 9

def main():
    N = int(input())
    MOD = 10**9 + 7
    # dp[i][j][k] := i桁目までで条件を満たす数の個数
    # j: 0が存在するかどうか
    # k: 9が存在するかどうか
    dp = [[[0] * 2 for _ in range(2)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(2):
                for l in range(10):
                    ni = i + 1
                    nj = j
                    nk = k
                    if l == 0:
                        nj = 1
                    if l == 9:
                        nk = 1
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= MOD
    ans = 0
    for j in range(2):
        for k in range(2):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    MOD = 10**9 + 7
    # dp[i][j] = j で終わる i 桁の数の個数
    dp = [[0] * 10 for _ in range(N+1)]
    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[N]) % MOD)
